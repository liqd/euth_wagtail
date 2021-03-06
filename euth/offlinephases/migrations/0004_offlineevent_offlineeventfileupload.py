# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 15:05
from __future__ import unicode_literals

import autoslug.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import euth.offlinephases.models
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('a4projects', '0014_collapsible_information_field'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('euth_offlinephases', '0003_change_document_and_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=120, verbose_name='Title')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a4projects.Project')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='OfflineEventFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=256)),
                ('document', models.FileField(upload_to=euth.offlinephases.models.document_path, validators=[
                    euth.contrib.validators.validate_file_type_and_size])),
                ('offlineevent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='euth_offlinephases.OfflineEvent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
