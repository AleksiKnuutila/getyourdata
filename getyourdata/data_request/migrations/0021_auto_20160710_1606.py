# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 16:06
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('data_request', '0020_auto_20160710_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqcontent',
            name='content',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='faqcontent',
            name='content_en',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='faqcontent',
            name='content_fi',
            field=tinymce.models.HTMLField(blank=True, default='', null=True),
        ),
    ]
