# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20171006_1712'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
