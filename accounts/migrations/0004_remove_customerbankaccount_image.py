# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-19 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_registercustomer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerbankaccount',
            name='Image',
        ),
    ]