# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0021_auto_20160706_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticationfield',
            name='help_text_en',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='authenticationfield',
            name='help_text_fi',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
