# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a4projects', '0014_collapsible_information_field'),
        ('home', '0033_translate_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helppages',
            name='flashpoll',
        ),
        migrations.AddField(
            model_name='helppages',
            name='a4_poll',
            field=models.ForeignKey(blank=True, help_text='Please select an exemplary a4-poll project.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='example_project_a4_poll', to='a4projects.Project'),
        ),
    ]
