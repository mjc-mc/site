# Generated by Django 2.2.9 on 2020-03-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0006_auto_20200301_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(blank=True, default='...', max_length=100, null=True, verbose_name='Nom'),
        ),
    ]
