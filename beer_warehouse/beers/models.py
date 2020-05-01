# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from utils import image_upload_location

class Company(models.Model):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Beer(models.Model):
    COLOR_YELLOW = 1
    COLOR_AMBER = 2
    COLOR_BRAWN = 3
    COLOR_BLACK = 4

    COLOR_CHOICES = (
        (COLOR_YELLOW , 'yellow'),
        (COLOR_AMBER , 'amber'),
        (COLOR_BRAWN , 'brawn'),
        (COLOR_BLACK , 'black'),
    )

    name = models.CharField('Name', max_length=50)
    alc = models.DecimalField('Alc', decimal_places=2, max_digits=5)
    is_filtered = models.BooleanField('Is filtered', default=False)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey(Company, related_name='beers')

    class Meta:
        verbose_name = 'Beer'
        verbose_name_plural = 'Beers'
        ordering = ['-name']

    def __str__(self):
        return self.name

class SpecialIngredient(models.Model):
    name = models.CharField('Name', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, related_name='Special_ingredients')

    class Meta:
        verbose_name = 'Special ingredient'
        verbose_name_plural = 'Special ingredients'
        ordering = ['-name']

    def __str__(self):
        return self.name