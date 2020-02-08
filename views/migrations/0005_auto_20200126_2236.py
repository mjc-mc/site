# Generated by Django 2.2.9 on 2020-01-26 22:36

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0004_pagesection'),
    ]

    operations = [
        migrations.AddField(
            model_name='slides',
            name='folder',
            field=models.CharField(blank=True, default='images/carousel/', editable=False, max_length=40, null=True, verbose_name='Folder'),
        ),
        migrations.AlterField(
            model_name='slides',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.upload_path_handler, verbose_name='Diapo - Image'),
        ),
    ]
