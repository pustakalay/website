# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-27 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
    ]
