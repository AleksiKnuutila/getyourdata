# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_request', '0011_auto_20160603_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfcontents',
            name='content1_en',
            field=models.TextField(blank=True, default='content eka', null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='content1_fi',
            field=models.TextField(blank=True, default='content eka', null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='content2_en',
            field=models.TextField(blank=True, default='content toka', null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='content2_fi',
            field=models.TextField(blank=True, default='content toka', null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='footer_en',
            field=models.CharField(blank=True, default='Regards,', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='footer_fi',
            field=models.CharField(blank=True, default='Regards,', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='header_en',
            field=models.CharField(blank=True, default='Dear recipient,', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pdfcontents',
            name='header_fi',
            field=models.CharField(blank=True, default='Dear recipient,', max_length=255, null=True),
        ),
    ]
