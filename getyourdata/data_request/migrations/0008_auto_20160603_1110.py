# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_request', '0007_auto_20160603_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfcontents',
            name='footer',
            field=models.CharField(blank=True, default='Regards,', max_length=255),
        ),
    ]
