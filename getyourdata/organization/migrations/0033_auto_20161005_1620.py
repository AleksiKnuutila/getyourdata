# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-05 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('organization', '0032_auto_20160903_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, help_text='A primary name', max_length=256, verbose_name='name')),
                ('identifier', models.CharField(blank=True, help_text='An issued identifier', max_length=512, verbose_name='identifier')),
                ('classification', models.CharField(blank=True, help_text='An area category, e.g. city', max_length=512, verbose_name='identifier')),
                ('geom', models.TextField(blank=True, help_text='A geometry', null=True, verbose_name='geom')),
                ('inhabitants', models.IntegerField(blank=True, help_text='The total number of inhabitants', null=True, verbose_name='inhabitants')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(blank=True, help_text='The area that contains this area', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='organization.Area')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='classification',
            field=models.CharField(blank=True, help_text='An organization category, e.g. committee', max_length=512, verbose_name='classification'),
        ),
        migrations.AddField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, help_text='An extended description of an organization', verbose_name='biography'),
        ),
        migrations.AddField(
            model_name='organization',
            name='freedom_of_information_flag',
            field=models.BooleanField(default=False, help_text='Whether organisation has duty to respond to Freedom of Information requests', verbose_name='Yes'),
        ),
        migrations.AddField(
            model_name='organization',
            name='nature_of_work',
            field=models.TextField(blank=True, help_text='A description of how data controller processes personal data', verbose_name='nature_of_work'),
        ),
        migrations.AddField(
            model_name='organization',
            name='summary',
            field=models.CharField(blank=True, help_text='A one-line description of an organization', max_length=1024, verbose_name='summary'),
        ),
        migrations.AddField(
            model_name='organizationdraft',
            name='classification',
            field=models.CharField(blank=True, help_text='An organization category, e.g. committee', max_length=512, verbose_name='classification'),
        ),
        migrations.AddField(
            model_name='organizationdraft',
            name='description',
            field=models.TextField(blank=True, help_text='An extended description of an organization', verbose_name='biography'),
        ),
        migrations.AddField(
            model_name='organizationdraft',
            name='freedom_of_information_flag',
            field=models.BooleanField(default=False, help_text='Whether organisation has duty to respond to Freedom of Information requests', verbose_name='Yes'),
        ),
        migrations.AddField(
            model_name='organizationdraft',
            name='nature_of_work',
            field=models.TextField(blank=True, help_text='A description of how data controller processes personal data', verbose_name='nature_of_work'),
        ),
        migrations.AddField(
            model_name='organizationdraft',
            name='summary',
            field=models.CharField(blank=True, help_text='A one-line description of an organization', max_length=1024, verbose_name='summary'),
        ),
        migrations.AddField(
            model_name='organization',
            name='area',
            field=models.ForeignKey(blank=True, help_text='The geographic area to which this organization is related', null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Area'),
        ),
        migrations.AddField(
            model_name='organizationdraft',
            name='area',
            field=models.ForeignKey(blank=True, help_text='The geographic area to which this organization is related', null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Area'),
        ),
    ]
