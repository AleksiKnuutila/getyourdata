# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-05 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0034_auto_20161005_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='end_date',
            new_name='dpa_registration_end_date',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='start_date',
            new_name='dpa_registration_start_date',
        ),
        migrations.RenameField(
            model_name='organizationdraft',
            old_name='end_date',
            new_name='dpa_registration_end_date',
        ),
        migrations.RenameField(
            model_name='organizationdraft',
            old_name='start_date',
            new_name='dpa_registration_start_date',
        ),
    ]
