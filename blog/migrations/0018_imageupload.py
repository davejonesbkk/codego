# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20161220_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=200)),
                ('image_file', models.ImageField(upload_to='')),
            ],
        ),
    ]
