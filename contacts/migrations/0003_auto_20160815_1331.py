# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20160815_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'managed': True, 'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='groupe',
            options={'managed': True, 'verbose_name': 'groupe', 'verbose_name_plural': 'groupes'},
        ),
        migrations.AlterModelTable(
            name='contact',
            table=None,
        ),
        migrations.AlterModelTable(
            name='emailaddress',
            table=None,
        ),
        migrations.AlterModelTable(
            name='groupe',
            table=None,
        ),
        migrations.AlterModelTable(
            name='phonenumber',
            table=None,
        ),
    ]
