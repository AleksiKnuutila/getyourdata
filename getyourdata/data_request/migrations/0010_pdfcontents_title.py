# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_request', '0009_auto_20160603_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfcontents',
            name='title',
            field=models.CharField(blank=True, default='Default', max_length=255, unique=True),
        ),
    ]