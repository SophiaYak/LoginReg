# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 13:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg_app', '0004_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
