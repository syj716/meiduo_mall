# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-15 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AreaModel',
            new_name='Area',
        ),
    ]
