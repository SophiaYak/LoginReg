# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg_app', '0006_auto_20170628_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
