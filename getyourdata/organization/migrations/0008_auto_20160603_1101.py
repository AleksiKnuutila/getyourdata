# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_auto_20160603_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticationfield',
            name='help_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='authenticationfield',
            name='validator_regex',
            field=models.CharField(blank=True, default='', max_length=1028),
        ),
    ]
