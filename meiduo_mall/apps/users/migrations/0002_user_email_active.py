# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-15 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_active',
            field=models.BooleanField(default=False, verbose_name='激活邮箱'),
        ),
    ]
