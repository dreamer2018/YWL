# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('sponsor', models.CharField(max_length=40)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='activity_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='donate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('time', models.DateTimeField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='donate_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='jobs_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='join',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('job', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('type', models.ForeignKey(to='ywl_site.jobs_type')),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
                ('read', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='news_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('url', models.URLField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='type',
            field=models.ForeignKey(to='ywl_site.news_type'),
        ),
        migrations.AddField(
            model_name='donate',
            name='type',
            field=models.ForeignKey(to='ywl_site.donate_type'),
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.ForeignKey(to='ywl_site.activity_type'),
        ),
    ]
