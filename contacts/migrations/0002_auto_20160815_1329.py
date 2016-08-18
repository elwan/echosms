# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'managed': True, 'ordering': ('prenom', 'nom'), 'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='emailaddress',
            options={'managed': True, 'verbose_name': 'Adresse email', 'verbose_name_plural': 'adresses emails'},
        ),
        migrations.AlterModelOptions(
            name='groupe',
            options={'managed': True, 'ordering': ('nom',), 'verbose_name': 'groupe', 'verbose_name_plural': 'groupes'},
        ),
        migrations.AlterModelOptions(
            name='phonenumber',
            options={'managed': True, 'verbose_name': 'Numero Telephone', 'verbose_name_plural': 'Numeros de Telephones'},
        ),
    ]
