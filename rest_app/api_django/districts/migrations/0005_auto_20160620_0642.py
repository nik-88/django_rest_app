# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 06:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0004_auto_20160620_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 6, 42, 29, 206326)),
        ),
        migrations.AlterField(
            model_name='district',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 6, 42, 29, 205655)),
        ),
    ]
