# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-15 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='区域')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='areas.AreaModel', verbose_name='父类区域')),
            ],
            options={
                'db_table': 'tb_areas',
            },
        ),
    ]