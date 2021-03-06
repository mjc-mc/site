# Generated by Django 2.2.9 on 2020-03-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0009_pagefile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagepseudostatic',
            options={'verbose_name': 'Page', 'verbose_name_plural': '2. Pages'},
        ),
        migrations.AlterModelOptions(
            name='slides',
            options={'verbose_name': 'Diapositive', 'verbose_name_plural': '1. Caroussel (Bandeau défilant)'},
        ),
        migrations.AlterField(
            model_name='pagepseudostatic',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nom'),
        ),
    ]
