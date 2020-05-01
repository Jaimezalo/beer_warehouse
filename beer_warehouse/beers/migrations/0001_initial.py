# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-01 17:09
from __future__ import unicode_literals

import beers.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('alc', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Alc')),
                ('is_filtered', models.BooleanField(default=False, verbose_name='Is filtered')),
                ('color', models.PositiveSmallIntegerField(choices=[(1, 'yellow'), (2, 'amber'), (3, 'brawn'), (4, 'black')], default=1, verbose_name='Color')),
                ('image', models.ImageField(blank=True, null=True, upload_to=beers.utils.image_upload_location, verbose_name='Image')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Beer',
                'verbose_name_plural': 'Beers',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='SpecialIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('beers', models.ManyToManyField(blank=True, related_name='Special_ingredients', to='beers.Beer')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'Special ingredient',
                'verbose_name_plural': 'Special ingredients',
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='beers.Company'),
        ),
    ]
