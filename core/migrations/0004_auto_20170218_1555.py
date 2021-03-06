# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170131_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '\u0423\u0447\u0435\u0431\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430', 'verbose_name_plural': '\u0423\u0447\u0435\u0431\u043d\u044b\u0435 \u0433\u0440\u0443\u043f\u043f\u044b'},
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0443\u0447\u0435\u0431\u043d\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u044b'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Department', verbose_name='\u0423\u0447\u0435\u0431\u043d\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430'),
        ),
    ]
