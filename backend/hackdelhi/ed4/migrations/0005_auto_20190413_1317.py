# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import ed4.models


class Migration(migrations.Migration):

    dependencies = [
        ('ed4', '0004_auto_20190413_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='document',
            field=models.FileField(blank=True, upload_to=ed4.models.custom_directory_path2),
        ),
    ]