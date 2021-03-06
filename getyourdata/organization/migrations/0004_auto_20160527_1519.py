# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20160527_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='address_line_one',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address_line_two',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='country',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email_address',
            field=models.EmailField(blank=True, default='', help_text='Email address used by the organization to respond to user data requests', max_length=255, null=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Postal code'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='verified',
            field=models.BooleanField(default=False, help_text='Verified organizations are visible to all users', verbose_name='Verified'),
        ),
        migrations.AddField(
            model_name='organization',
            name='authentication_fields',
            field=models.ManyToManyField(related_name='_organization_authentication_fields_+', to='organization.AuthenticationField'),
        ),
    ]
