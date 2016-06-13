__author__ = 'stikks'
# import django core modules
from django.contrib.auth.models import User
from django.core.serializers.python import Serializer

# import third party/django extensions modules
from rest_framework import serializers, validators

# import project modules
from .models import TransportationProvider, ServiceArea, Currency, Language


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'code')
        model = None

    def create(self, validated_data):
        if self.Meta.model is None:
            raise NotImplementedError
        return self.Meta.model.objects.create(**validated_data)

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
        fields = ("id", 'name', 'email', 'phone', 'language', 'currency', 'date_created', 'date_modified')
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
                fields=('name', 'transport_provider', 'polygon')
            )
        ]

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.polygon = validated_data.get('polygon', instance.email)
        instance.transport_provider = validated_data.get('transport_provider', instance.phone)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class QuerySerializer(serializers.Serializer):
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)


class NewServiceAreaSerializer(serializers.Serializer):
    """ Serializer class for creating new service areas """
    name = serializers.CharField(required=True, help_text="service area name")
    polygon = serializers.CharField(required=True, help_text="jsonified polygon object")
    authorization_token = serializers.CharField(required=True, help_text="Transport provider authorization token")
    price = serializers.FloatField(required=True, help_text="service area price")
    transport_provider = serializers.CharField(read_only=True)


class ServiceListSerializer(serializers.Serializer):
    authorization_token = serializers.CharField(required=True, help_text="Transport provider authorization token")


# class UserSerializer(serializers.ModelSerializer):
    # transport_providers = serializers.PrimaryKeyRelatedField(many=True, queryset=TransportationProvider.objects.all())
    #w
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'transport_providers')