# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-19 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20171219_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/%Y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]
