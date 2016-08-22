# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 12:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100, verbose_name='prenom')),
                ('nom', models.CharField(max_length=200, verbose_name='nom')),
                ('about', models.TextField(blank=True, verbose_name='about')),
                ('photo', models.ImageField(blank=True, upload_to='contacts/person/', verbose_name='photo')),
                ('pays', django_countries.fields.CountryField(max_length=2)),
                ('numero_telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email_address', models.EmailField(max_length=254, verbose_name='Adresse Email')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_groupe', models.CharField(max_length=200, verbose_name='Nom')),
                ('about', models.TextField(blank=True, verbose_name='about')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('groupe_utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'contacts_groups',
                'verbose_name': 'groupe',
                'verbose_name_plural': 'groupes',
                'ordering': ('nom_groupe',),
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_groupe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Groupe', verbose_name='Groupe'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
