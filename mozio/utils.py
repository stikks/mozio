__author__ = 'stikks'

from .settings import LANGUAGES, CURRENCIES
from app.serializers import LanguageSerializer, CurrencySerializer


def create_currencies():
    for element in CURRENCIES:
        lower_cased = element.copy()
        for key, value in element:
            lower_cased[key] = value.lower()
        serializer = CurrencySerializer(data=element)
        if serializer.is_valid():
            serializer.save()

    return True


def create_languages():
    for element in LANGUAGES:
        lower_cased = element.copy()
        for key, value in element:
            lower_cased[key] = value.lower()
        serializer = LanguageSerializer(data=element)
        if serializer.is_valid():
            serializer.save()

    return True