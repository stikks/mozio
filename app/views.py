import json

# import django core modules
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.gis.geos import Polygon, Point

# import third party/django extensions modules
from rest_framework import decorators, response, reverse, generics, status, permissions

# import application
from .serializers import CurrencySerializer, TransportProviderSerializer, LanguageSerializer, ServiceAreaSerializer, \
    UserSerializer
from .permissions import IsOwnerorReadOnly


# Create your views here.
@decorators.api_view(["GET"])
def api_root(request, format=None):
    return response.Response({
        'transport-providers': reverse.reverse('transport-providers', request=request, format=format),
        'currencies': reverse.reverse('currencies', request=request, format=format),
        'languages': reverse.reverse('languages', request=request, format=format)
    })


class CurrencyList(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = CurrencySerializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class LanguageList(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer
    queryset = LanguageSerializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TransportProviderList(generics.ListCreateAPIView):
    serializer_class = TransportProviderSerializer
    queryset = TransportProviderSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerorReadOnly,)

    def post(self, request, *args, **kwargs):

        data = request.data

        language_name = data.get("language")

        if not language_name:
            return response.Response({"error": "language parameter missing"}, status=status.HTTP_400_BAD_REQUEST)

        language = LanguageSerializer.Meta.model.objects.filter(name__iexact=language_name).first()

        if not language:
            return response.Response({"error": "language not found. please contact an administrator to help "
                                               "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)

        data["language"] = language.pk

        currency_name = data.get("currency")

        if not currency_name:
            return response.Response({"error": "currency parameter missing"}, status=status.HTTP_400_BAD_REQUEST)

        currency = CurrencySerializer.Meta.model.objects.filter(Q(name__contains=currency_name.lower()) |
                                                                Q(name__iexact=currency_name.lower())).first()

        if not currency:
            return response.Response({"error": "currency not found. please contact an administrator to help "
                                               "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)

        data["currency"] = currency.pk
        data["owner"] = self.request.user.pk

        serializer = TransportProviderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransportProviderSerializer
    queryset = TransportProviderSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerorReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ServiceAreaList(generics.ListCreateAPIView):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceAreaSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerorReadOnly,)

    def get(self, request, *args, **kwargs):
        token = request.query_params.get("token")
        if not token:
            return response.Response({"detail": "invalid or missing authorization token"}, status=status.HTTP_403_FORBIDDEN)
        areas = ServiceAreaSerializer.Meta.model.objects.filter(transport_provider=kwargs.get('pk')).all()
        serializer = ServiceAreaSerializer(areas, many=True)
        return response.Response({"count": len(serializer.data), "next": None, "previous": None, "results": serializer.data})

    def post(self, request, *args, **kwargs):

        data = request.data or request.query_params

        token = request.query_params.get("token") or request.data.get("token")
        if not token:
            return response.Response({"detail": "invalid or missing authorization token"}, status=status.HTTP_403_FORBIDDEN)

        provider_id = kwargs.pop("pk")

        provider = TransportProviderSerializer.Meta.model.objects.filter(pk=provider_id).first()

        if not provider:
            return response.Response({"error": "Transport Provider not found"}, status=status.HTTP_404_NOT_FOUND)

        data["transport_provider"] = provider.pk

        polygon_info = data.get('geojson_data')

        if not polygon_info:
            return response.Response({"error": "Polygon info missing"}, status=status.HTTP_404_NOT_FOUND)

        polygon_data = json.loads(polygon_info)
        line = Polygon(polygon_data)

        data["polygon"] = line
        data["owner"] = self.request.user.pk

        serializer = ServiceAreaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaQuery(generics.RetrieveAPIView):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceAreaSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerorReadOnly,)

    def post(self, request, *args, **kwargs):

        longitude = request.data.get('longitude')

        if not longitude:
            return response.Response({"error": "longitude missing"}, status=status.HTTP_400_BAD_REQUEST)

        latitude = request.data.get('latitude')

        if not latitude:
            return response.Response({"error": "latitude missing"}, status=status.HTTP_400_BAD_REQUEST)

        polygon = Point(latitude, longitude)
        areas = ServiceAreaSerializer.Meta.model.objects.filter(polygon__contains=polygon).all()
        serializer = ServiceAreaSerializer(areas, many=True)
        return response.Response({"count": len(serializer.data), "next": None, "previous": None, "results": serializer.data})


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceAreaSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerorReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer