# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=128, unique=True),
        ),
    ]
