# import django core modules
from django.contrib.auth.models import User

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
        'service-areas': reverse.reverse('service-areas', request=request, format=format),
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


class TranportProviderList(generics.ListCreateAPIView):
    serializer_class = TransportProviderSerializer
    queryset = TransportProviderSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerorReadOnly,)

    def post(self, request, *args, **kwargs):

        data = request.data

        language_name = data.get("language")

        print "data", data
        print "language_name", language_name

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

        currency = CurrencySerializer.Meta.model.objects.filter(name__contains=currency_name).first()

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

    def get(self, request, *args, **kwargs):
        print 'kwargs', kwargs
        areas = ServiceAreaSerializer.Meta.model.objects.filter(transport_provider=kwargs.get('pk')).all()
        serializer = ServiceAreaSerializer(areas, many=True)
        return response.Response({"count": len(serializer.data), "next": None, "previous": None, "results": serializer.data})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceAreaSerializer.Meta.model.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerorReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer