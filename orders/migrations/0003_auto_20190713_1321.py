# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-13 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_ownbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='grade',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='school',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
