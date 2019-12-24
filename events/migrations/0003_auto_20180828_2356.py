# Generated by Django 2.0.7 on 2018-08-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180828_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_and_time',
            field=models.CharField(max_length=200, null=True, verbose_name='Date(s) & Heure(s)'),
        ),
        migrations.AddField(
            model_name='event',
            name='rate',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tarifs'),
        ),
        migrations.AlterField(
            model_name='event',
            name='contact',
            field=models.CharField(blank=True, max_length=100, verbose_name='Personne à contacter'),
        ),
    ]
