# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-19 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20171219_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirrelation',
            name='next_dir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_dir', to='article.Dir', verbose_name='\u540e\u4e00\u4e2a\u76ee\u5f55'),
        ),
        migrations.AlterField(
            model_name='dirrelation',
            name='pre_dir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_dir', to='article.Dir', verbose_name='\u524d\u4e00\u4e2a\u76ee\u5f55'),
        ),
        migrations.AlterField(
            model_name='subdirrelation',
            name='next_subDdir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_subDir', to='article.SubDir', verbose_name='\u540e\u4e00\u4e2a\u76ee\u5f55'),
        ),
        migrations.AlterField(
            model_name='subdirrelation',
            name='pre_subDir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_subDir', to='article.SubDir', verbose_name='\u524d\u4e00\u4e2a\u76ee\u5f55'),
        ),
    ]