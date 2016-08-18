# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(unique=True, max_length=11)),
                ('passwd', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=10, blank=True)),
                ('address', models.CharField(max_length=40, blank=True)),
                ('about', models.TextField()),
            ],
        ),
    ]
