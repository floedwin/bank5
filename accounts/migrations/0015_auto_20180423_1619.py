# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-23 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20180423_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registercustomertranscations',
            old_name='transcation_date',
            new_name='Transcation_date',
        ),
    ]