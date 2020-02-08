# Generated by Django 2.2.9 on 2020-01-26 22:36

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_activity_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_animation',
            name='folder',
            field=models.CharField(blank=True, default='images/activity/animation/', editable=False, max_length=40, null=True, verbose_name='Folder'),
        ),
        migrations.AddField(
            model_name='activity_animation_type',
            name='folder',
            field=models.CharField(blank=True, default='images/activity/animation_type', editable=False, max_length=40, null=True, verbose_name='Folder'),
        ),
        migrations.AddField(
            model_name='elements_type',
            name='folder',
            field=models.CharField(blank=True, default='images/event_type', editable=False, max_length=40, null=True, verbose_name='Folder'),
        ),
        migrations.AddField(
            model_name='host',
            name='folder',
            field=models.CharField(blank=True, default='images/hosts/', editable=False, max_length=40, null=True, verbose_name='Folder'),
        ),
        migrations.AlterField(
            model_name='activity_animation',
            name='image',
            field=models.ImageField(default='noimage.jpg', upload_to=utils.upload_path_handler, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='activity_animation_type',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.upload_path_handler, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='elements_type',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.upload_path_handler, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='host',
            name='image',
            field=models.ImageField(default='noimage.jpg', upload_to=utils.upload_path_handler, verbose_name='Image'),
        ),
    ]
