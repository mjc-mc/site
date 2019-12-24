# Generated by Django 2.0.7 on 2018-08-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20180826_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity_animation_slot',
            name='flash',
        ),
        migrations.AddField(
            model_name='activity_animation',
            name='flash',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Info flash'),
        ),
    ]
