# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20160815_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupe',
            options={'managed': True, 'ordering': ('nom_groupe',), 'verbose_name': 'groupe', 'verbose_name_plural': 'groupes'},
        ),
    ]