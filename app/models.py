import hashlib, uuid

from django.db import models
from django.contrib.gis.db.models import PolygonField


# Create your models here.
class AbstractClass(models.Model):
    """
    Abstract base model class
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('date_created',)


class Language(AbstractClass):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False)
    code = models.CharField(max_length=10, blank=False)


class Currency(AbstractClass):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False)
    symbol = models.CharField(max_length=25)
    code = models.CharField(max_length=10, blank=False)


class TransportationProvider(AbstractClass):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=50, blank=False)
    language = models.ForeignKey(Language)
    currency = models.ForeignKey(Currency)
    authorization_token = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='transport_providers')

    @classmethod
    def generate_token(self, email):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + email.encode()).hexdigest()


class ServiceArea(AbstractClass):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    price = models.FloatField(blank=False)
    geojson_data = PolygonField(blank=False)
    transport_provider = models.ForeignKey(TransportationProvider)