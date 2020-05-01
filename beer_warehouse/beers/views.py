# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from models import Beer


def beer_list_view(request, ):
    beer_list = Beer.objects.all()
    context = {
        'beer_list': beer_list
    }

    return render(request, 'beer.list.html', context)


def beer_detail_view(request, pk):
    context = {
        'beer': Beer.objects.get(pk=pk)
    }

    return render(request, 'beer.details.html', context)
