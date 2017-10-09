# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 17:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20171003_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=1)),
                ('title', models.CharField(default='Defaul Title', max_length=200)),
                ('body', models.TextField(default='Body of post goes here')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_date',
            field=models.DateField(default=datetime.date(2017, 10, 6)),
        ),
    ]
