# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicearea',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='transportationprovider',
            name='owner',
        ),
    ]