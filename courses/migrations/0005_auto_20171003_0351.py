# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170921_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_date',
            field=models.DateField(default=datetime.date(2017, 10, 3)),
        ),
    ]
