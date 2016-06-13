import json

# import django core modules
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.gis.geos import Polygon, Point

# import third party/django extensions modules
from rest_framework import decorators, response, reverse, generics, status, views

# import application
from .serializers import CurrencySerializer, TransportProviderSerializer, LanguageSerializer, ServiceAreaSerializer, \
    QuerySerializer, ServiceListSerializer, NewServiceAreaSerializer
from .models import ServiceArea, TransportationProvider


# Create your views here.
@decorators.api_view(["GET"])
def api_root(request, format=None):
    return response.Response({
        'transport-providers': reverse.reverse('transport-providers', request=request, format=format),
        'currencies': reverse.reverse('currencies', request=request, format=format),
        'languages': reverse.reverse('languages', request=request, format=format),
        'service-areas': reverse.reverse('service-areas', request=request, format=format),
        'new-service-areas': reverse.reverse('new-service-areas', request=request, format=format)
    })


class CurrencyList(generics.ListCreateAPIView):
    """Get the list of currencies from the database."""

    serializer_class = CurrencySerializer
    queryset = CurrencySerializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class LanguageList(generics.ListCreateAPIView):
    """Get the list of languages from the database."""
    serializer_class = LanguageSerializer
    queryset = LanguageSerializer.Meta.model.objects.all()

    def post(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TransportProviderList(generics.ListCreateAPIView):
    """Get the list of transportation providers from the database."""
    serializer_class = TransportProviderSerializer
    queryset = TransportProviderSerializer.Meta.model.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerorReadOnly,)

    def post(self, request, *args, **kwargs):

        data = request.data.copy()

        language_name = data.get("language")

        if not language_name:
            return response.Response({"error": "language parameter missing"}, status=status.HTTP_400_BAD_REQUEST)

        language = LanguageSerializer.Meta.model.objects.filter(name__iexact=language_name).first()

        if not language:
            return response.Response({"error": "language not found. please contact an administrator to help "
                                               "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)

        data["language"] = language.id

        currency_name = data.get("currency")

        if not currency_name:
            return response.Response({"error": "currency parameter missing"}, status=status.HTTP_400_BAD_REQUEST)

        currency = CurrencySerializer.Meta.model.objects.filter(Q(name__contains=currency_name.lower()) |
                                                                Q(name__iexact=currency_name.lower())).first()

        if not currency:
            return response.Response({"error": "currency not found. please contact an administrator to help "
                                               "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)

        data["currency"] = currency.pk

        serializer = TransportProviderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data["authorization_token"] = TransportProviderSerializer.Meta.model.objects.\
                get(pk=response_data["id"]).authorization_token
            return response.Response(response_data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransportProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """Return the details on a transportation provider."""
    serializer_class = TransportProviderSerializer
    queryset = TransportProviderSerializer.Meta.model.objects.all()

    def put(self, request, *args, **kwargs):

        provider_id = kwargs.get("pk")

        provider = TransportProviderSerializer.Meta.model.objects.get(pk=provider_id)

        if not provider:
            return response.Response({"error": "Transport Provider not found. please contact an administrator to help "
                                               "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        language_name = data.get("language")

        if language_name:
            language = LanguageSerializer.Meta.model.objects.filter(name__iexact=language_name).first()

            if not language:
                return response.Response({"error": "language not found. please contact an administrator to help "
                                                   "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)
            else:
                data["language"] = language.id

        currency_name = data.get("currency")

        if currency_name:

            currency = CurrencySerializer.Meta.model.objects.filter(Q(name__contains=currency_name.lower()) |
                                                                Q(name__iexact=currency_name.lower())).first()

            if not currency:
                return response.Response({"error": "currency not found. please contact an administrator to help "
                                                   "in setting up your account"}, status=status.HTTP_404_NOT_FOUND)

            else:
                data["currency"] = currency.pk

        serializer = TransportProviderSerializer(provider, data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaList(generics.GenericAPIView):
    """
     Retrieves a list of service areas for a particular transport provider.
     """
    serializer_class = ServiceListSerializer

    def post(self, request, *args, **kwargs):

        data = request.data.copy()

        token = data.get("authorization_token")

        provider = TransportProviderSerializer.Meta.model.objects.filter(authorization_token__iexact=token).first()

        if not provider:
            return response.Response({"error": "Transport Provider not found"}, status=status.HTTP_404_NOT_FOUND)

        areas = ServiceArea.objects.filter(transport_provider=provider.pk).all()

        serializer = ServiceAreaSerializer(areas, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)


class NewServiceArea(generics.GenericAPIView):
    """
     Creates a new service area for a particular transport provider.
     """
    serializer_class = NewServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    def post(self, request, *args, **kwargs):

        token = request.data.get("authorization_token")

        provider = TransportProviderSerializer.Meta.model.objects.filter(authorization_token__iexact=token).first()

        if not provider:
            return response.Response({"error": "Transport Provider not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            polygon = request.data.get("polygon")

            print polygon

            polygon_data = json.loads(polygon)

            line = Polygon(polygon_data)

            data = {
                "name": request.data.get("name"),
                "price": request.data.get("price"),
                "polygon": line,
                "transport_provider": provider.pk
            }

            serializer = ServiceAreaSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                response_data = serializer.data.copy()
                response_data["transport_provider"] = provider.name
                return response.Response(response_data, status=status.HTTP_200_OK)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({"error": "Invalid input polygon parameters"}, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Updating field information of a particular service area"""
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

    def put(self, request, *args, **kwargs):

        data = request.data.copy()

        provider_name = data.get("transport_provider")
        provider = TransportationProvider.objects.filter(name__iexact=provider_name).first()

        if not provider:
            return response.Response({"error": "Transport Provider not found"}, status=status.HTTP_404_NOT_FOUND)

        data["transport_provider"] = provider.pk

        serializer = ServiceAreaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryView(generics.GenericAPIView):
    """ Returns a list of service areas matching the geometric point created by a lat/lng pair"""
    serializer_class = QuerySerializer
    queryset = ServiceArea.objects.all()

    def post(self, request, *args, **kwargs):

        try:
            latitude = request.data.get("latitude")

            longitude = request.data.get("longitude")

            point = Point(float(latitude), float(longitude))

            areas = ServiceArea.objects.filter(polygon__contains=point).all()

            serializer = ServiceAreaSerializer(areas, many=True)

            return response.Response(
                {"count": len(serializer.data), "next": None, "previous": None, "results": serializer.data})
        except:
            return response.Response({"error": "Invalid input parameters"}, status=status.HTTP_400_BAD_REQUEST)

