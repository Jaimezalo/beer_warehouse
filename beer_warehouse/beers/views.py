# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def first_view(request):
    my_var = "Hola"
    context = {
        'my_var': my_var,
    }

    return render(request, 'beers.html', context)
