# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 08:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0006_auto_20160620_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='Campuses',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='campus',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 8, 48, 4, 198574)),
        ),
        migrations.AlterField(
            model_name='district',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 8, 48, 4, 197875)),
        ),
    ]
