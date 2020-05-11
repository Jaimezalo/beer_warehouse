# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from utils import image_upload_location

COMPANIA = (('s', 'Sol@'), ('a', 'Amig@s'), ('f', 'Familia'), ('p', 'Pareja'))
TIPO = (('i', 'Interior'), ('c', 'Costa'))
AFLUENCIA = (('m', 'Media'), ('b', 'Baja'), ('a', 'Alta'))
PRECIO = (('$', 'Barato'), ('$$', 'Medio'), ('$$$', 'Caro'))

class Destino(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    compania = models.CharField(max_length=1, choices=COMPANIA)
    tipo = models.CharField(max_length=1, choices=TIPO)
    afluencia = models.CharField(max_length=1, choices=AFLUENCIA)
    precio = models.CharField(max_length=1, choices=PRECIO)
    tipoTurismo = models.CharField('Tipo turismo', max_length=50)
    descripcion = models.CharField('Descripcion', max_length=250)
    coordenadas = models.CharField('Coordenadas', max_length=50)
    link = models.CharField('Link', max_length=50)

    class Meta:
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre
