# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-05 22:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0039_auto_20161005_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='area',
            new_name='jurisdiction',
        ),
        migrations.RenameField(
            model_name='organizationdraft',
            old_name='area',
            new_name='jurisdiction',
        ),
    ]
