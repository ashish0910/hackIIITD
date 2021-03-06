# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='word_to_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to='custom_directory_path')),
                ('text', models.TextField(blank=True, max_length=2000)),
                ('video', models.FileField(blank=True, upload_to='custom_directory_path')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
