# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 04:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171018_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
