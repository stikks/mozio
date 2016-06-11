__author__ = 'stikks'
# import django core modules
from django.contrib.auth.models import User

# import third party/django extensions modules
from rest_framework import serializers, validators

# import project modules
from .models import TransportationProvider, ServiceArea, Currency, Language


def lower_case_dict_values(data):

    dict_data = dict(data)
    new_data = dict_data.copy()
    for key, value in new_data.items():
        if isinstance(value, str):
            new_data[key] = value.lower()

    return new_data


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'code')
        model = None

    def create(self, validated_data):
        if self.Meta.model is None:
            raise NotImplementedError
        data = lower_case_dict_values(validated_data)
        return self.Meta.model.objects.create(**data)

    def update(self, instance, validated_data):
        if self.Meta.model is None:
            raise NotImplementedError
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data('code', instance.code)
        instance.save()
        return instance


class CurrencySerializer(BaseSerializer):
    class Meta:
        model = Currency
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'code')
            )
        ]

class LanguageSerializer(BaseSerializer):
    class Meta:
        model = Language
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'code')
            )
        ]


class TransportProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationProvider
        fields = ("id", 'name', 'email', 'phone', 'language', 'currency', 'date_created', 'date_modified', 'owner')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'email', 'phone')
            )
        ]

    def create(self, validated_data):
        authorization_token = self.Meta.model.generate_token(validated_data['email'])
        validated_data["authorization_token"] = authorization_token
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.language = validated_data.get('language', instance.language)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.save()
        return instance


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('name', 'transport_provider', 'price', 'polygon')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('name', 'price', 'transport_provider', 'polygon')
            )
        ]

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.transport_provider = validated_data('transport_provider', instance.transport_provider)
        instance.price = validated_data.get('price', instance.price)
        instance.polygon = validated_data.get('polygon', instance.polygon)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    transport_providers = serializers.PrimaryKeyRelatedField(many=True, queryset=TransportationProvider.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'transport_providers')