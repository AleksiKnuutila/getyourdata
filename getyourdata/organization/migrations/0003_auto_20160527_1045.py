# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20160527_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='email',
            new_name='email_address',
        ),
    ]
