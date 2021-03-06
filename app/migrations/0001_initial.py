# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 17:28
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('symbol', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransportationProvider',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('authorization_token', models.TextField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Currency')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Language')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transport_providers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='servicearea',
            name='transport_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TransportationProvider'),
        ),
    ]
