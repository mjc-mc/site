# Generated by Django 2.0.7 on 2018-08-26 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0012_auto_20180826_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop_Animation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('disabled_friendly', models.BooleanField(default=None, verbose_name='Accessible handicap')),
                ('new', models.BooleanField(default=None, verbose_name='Nouveau')),
                ('available_in_both_cities', models.BooleanField(default=None, verbose_name='Existe à Mauguio ET à Carnon')),
                ('image', models.ImageField(default='noimage.jpg', upload_to='images/workshop/animation/', verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='Présentation générale')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes spécifiques')),
            ],
            options={
                'verbose_name': 'Atelier - Animation',
                'verbose_name_plural': '2. Ateliers - Animation',
            },
        ),
        migrations.CreateModel(
            name='Workshop_Animation_Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Nom')),
                ('new', models.BooleanField(default=None, verbose_name='Nouveau')),
                ('level', models.CharField(blank=True, max_length=50, null=True, verbose_name='Niveau')),
                ('dates', models.TextField(blank=True, null=True, verbose_name='Dates & Horaires')),
                ('date_of_the_last_day', models.DateField(verbose_name='Date du dernier jour')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Présentation générale')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes particulières')),
                ('rate', models.TextField(blank=True, null=True, verbose_name='Tarifs')),
                ('age_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Workshop', to='activities.Age_Group')),
                ('host', models.ManyToManyField(blank=True, related_name='Workshop', to='activities.Host')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Workshop', to='activities.Room')),
                ('workshop_animation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Workshop', to='workshops.Workshop_Animation')),
            ],
            options={
                'verbose_name': 'Atelier - Créneau',
                'verbose_name_plural': '3. Ateliers - Créneaux',
            },
        ),
        migrations.CreateModel(
            name='Workshop_Animation_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animation_type', models.CharField(max_length=100, verbose_name="Type d'animation")),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/workshop/animation_type', verbose_name='Image')),
            ],
            options={
                'verbose_name': "Atelier - Type d'animation",
                'verbose_name_plural': "1. Ateliers - Types d'animations",
            },
        ),
        migrations.AddField(
            model_name='workshop_animation',
            name='animation_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Animation', to='workshops.Workshop_Animation_Type'),
        ),
    ]
