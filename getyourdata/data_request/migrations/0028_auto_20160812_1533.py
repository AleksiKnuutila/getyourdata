# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_request', '0027_auto_20160812_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmessagecontent',
            name='name_en',
            field=models.TextField(default='Default', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='feedbackmessagecontent',
            name='name_fi',
            field=models.TextField(default='Default', null=True, unique=True),
        ),
    ]
