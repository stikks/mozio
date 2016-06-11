__author__ = 'stikks'
# import django core modules
from django.contrib.auth.models import User

# import third party/django extensions modules
from rest_framework import serializers

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


class LanguageSerializer(BaseSerializer):
    class Meta:
        model = Language


class TransportProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationProvider
        fields = ("id", 'name', 'email', 'phone', 'language', 'currency', 'date_created', 'date_modified', 'owner')

    def create(self, validated_data):
        authorization_token = self.Meta.model.generate_token(validated_data['email'])
        validated_data["authorization_token"] = authorization_token
        print validated_data, 'valid'
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
        fields = ('name', 'transport_provider', 'price', 'geojson_data')

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.transport_provider = validated_data('transport_provider', instance.transport_provider)
        instance.price = validated_data.get('price', instance.price)
        instance.geojson_data = validated_data.get('name', instance.geojson_data)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    transport_providers = serializers.PrimaryKeyRelatedField(many=True, queryset=TransportationProvider.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'transport_providers')