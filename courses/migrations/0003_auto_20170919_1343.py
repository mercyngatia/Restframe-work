# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170919_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='availability',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(max_length=50),
        ),
    ]