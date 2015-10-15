# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('slug', models.CharField(max_length=256, db_index=True, verbose_name='网址')),
                ('content', models.TextField(default='', blank=True, verbose_name='内容')),
                ('published', models.BooleanField(default=True, verbose_name='正式发布')),
                ('author', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '教程',
                'verbose_name': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='栏目名称')),
                ('slug', models.CharField(max_length=256, db_index=True, verbose_name='栏目网址')),
                ('intro', models.TextField(default='', verbose_name='栏目简介')),
            ],
            options={
                'verbose_name_plural': '栏目',
                'verbose_name': '栏目',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name='归属栏目'),
        ),
    ]
