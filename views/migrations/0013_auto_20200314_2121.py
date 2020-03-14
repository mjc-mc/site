# Generated by Django 2.2.9 on 2020-03-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0012_auto_20200314_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpagemessage',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='landingpagemessage',
            name='category',
            field=models.CharField(choices=[('info', 'INFO (Bleu)'), ('success', 'POSITIF (Vert)'), ('warning', 'ATTENTION (Orange)'), ('danger', 'DANGER (Rouge)')], default='info', max_length=100, null=True, verbose_name='Couleur'),
        ),
    ]