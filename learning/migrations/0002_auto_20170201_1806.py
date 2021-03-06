# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 15:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='\u041e\u0442\u0432\u0435\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f')),
                ('is_correct', models.BooleanField(default=False, verbose_name='\u0412\u0435\u0440\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442?')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u0430',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0)),
                ('question_count', models.PositiveIntegerField(default=0)),
                ('complete', models.BooleanField(default=False)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0442\u0435\u0441\u0442\u0430')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u0430')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0442\u0435\u0441\u0442\u0430',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0442\u0435\u0441\u0442\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='\u0412\u0435\u0440\u043d\u044b\u0439?'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning.Question', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='questionresult',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Question', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
        ),
        migrations.AddField(
            model_name='questionresult',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.UserResult', verbose_name='\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f'),
        ),
    ]
