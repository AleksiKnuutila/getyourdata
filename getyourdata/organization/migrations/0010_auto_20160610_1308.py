# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticationfield',
            name='validator_regex',
            field=models.CharField(blank=True, default='', help_text='If not blank, this regex is used to validate the field value', max_length=1028),
        ),
    ]
