# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 17:04
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_auto_20160815_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailaddress',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='content_type',
        ),
        migrations.AddField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(default='elwan7@gmail.com', max_length=254, verbose_name='Adresse Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='numero_telephone',
            field=models.CharField(default=774215209, max_length=1000, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.", regex='^(7\\d{8},?)+$')], verbose_name='Numero Téléphone'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EmailAddress',
        ),
        migrations.DeleteModel(
            name='PhoneNumber',
        ),
    ]