# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 09:27
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161216_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
