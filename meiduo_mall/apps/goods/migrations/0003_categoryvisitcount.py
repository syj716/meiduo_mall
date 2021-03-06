# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-07 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200117_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryVisitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='访问量')),
                ('date', models.DateField(verbose_name='访问日期')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品分类')),
            ],
            options={
                'db_table': 'tb_category_visit_count',
            },
        ),
    ]
