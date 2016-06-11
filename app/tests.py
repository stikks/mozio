# import core django modules
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# import django extensions modules
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate
from rest_framework import status

# Create your tests here.
from .models import TransportationProvider, ServiceArea, Currency, Language
import views

factory = APIRequestFactory()


# models test
class CurrencyTest(TestCase):

    def create_currency(self, code="test", name="yes, this is only a test", symbol="symbol"):
        return Currency.objects.create(code=code, name=name, symbol=symbol)

    def test_currency_creation(self):
        w = self.create_currency()
        self.assertTrue(isinstance(w, Currency))


class LanguageTest(TestCase):

    def create_language(self, code="language", name="yes, this is a language"):
        return Language.objects.create(code=code, name=name)

    def test_language_creation(self):
        w = self.create_language()
        self.assertTrue(isinstance(w, Language))


class CurrencyTests(APITestCase):
    def test_create_currency(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('currencies')
        data = {'name': 'Sumerian', 'code': 'SUM', 'symbol': 'symbol'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve_currencies(self):
        """
        Ensure we can update a currency object.
        """
        currencies = Currency.objects.all()
        url = reverse('currencies')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LanguageTests(APITestCase):
    def test_create_language(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('languages')
        data = {'name': 'Sumerian', 'code': 'SUM'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve_languages(self):
        """
        Ensure we can update a currency object.
        """
        currencies = Language.objects.all()
        url = reverse('languages')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TransportProviderTests(APITestCase):
    def test_create_transport_provider_without_authentication(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('transport-providers')
        data = {'name': 'Marvel Studios', 'email': 'marvel@studios.com', 'phone': '0987654321', 'language': 'igbo',
                'currency': 'pound'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create_object():
        user = User.objects.create(username="admin", password="admin")
        language = Language.objects.create(name="Igbo", code="IGB")
        currency = Currency.objects.create(name="Naira", code="NGN", symbol="Nigeria Naira")
        view = views.TransportProviderList.as_view()
        factory = APIRequestFactory()
        data = {'name': 'Marvel Studios', 'email': 'marvel@studios.com', 'phone': '0987654321', 'language': 'igbo',
                'currency': 'naira'}
        request = factory.post('/ap1/v1/transport-providers', data=data)
        force_authenticate(request, user=user)
        response = view(request)

        return response

    def test_create_transport_provider_with_authentication(self):
        """
        Ensure we can create a new account object.
        """
        response = self.create_object()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_providers(self):
        """
        Ensure we can update a currency object.
        """
        user = User.objects.create(username="admin", password="admin")
        view = views.TransportProviderList.as_view()
        factory = APIRequestFactory()
        request = factory.get('/ap1/v1/transport-providers')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# class ServiceAreaTests(APITestCase):
    # def test_create_service_area_without_authentication(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     user = User.objects.filter(username="admin").first()
    #     TransportProviderTests.create_object()
    #     view = views.TranportProviderList.as_view()
    #     factory = APIRequestFactory()
    #     data = {'name': 'Yaba', 'price': '1000', 'geo_json_data': ((0, 0), (0, 1), (1, 1), (0, 0))}
    #     request = factory.post('/ap1/v1/transport-providers/1/service-areas', data=data)
    #     # force_authenticate(request, user=user)
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    # def test_create_service_area_with_authentication(self):
    #     """
    #     Ensure we can create a new account object.
    #     """
    #     user = User.objects.create(username="admin", password="admin")
    #     language = Language.objects.create(name="Igbo", code="IGB")
    #     currency = Currency.objects.create(name="Naira", code="NGN", symbol="Nigeria Naira")
    #     view = views.TranportProviderList.as_view()
    #     factory = APIRequestFactory()
    #     data = {'name': 'Marvel Studios', 'email': 'marvel@studios.com', 'phone': '0987654321', 'language': 'igbo',
    #             'currency': 'naira'}
    #     request = factory.post('/ap1/v1/transport-providers', data=data)
    #     force_authenticate(request, user=user)
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)