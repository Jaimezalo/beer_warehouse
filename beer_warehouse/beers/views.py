# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from models import Beer


@login_required
def beer_list_view(request):
    context = {'beer_list': Beer.objects.all()}
    return render(request, 'beer.list.html', context)

class BeerListView(LoginRequiredMixin, ListView):
    model = Beer


@login_required
def beer_detail_view(request, pk):
    BEER = Beer.objects.get(pk=pk)

    name = BEER.name
    alc = BEER.alc
    color = BEER.color
    company = BEER.company
    image = BEER.image
    context = {
        'beer_name': name,
        'beer_alc': alc,
        'beer_color': color,
        'beer_company': company,
        'beer_image': image,

    }

    return render(request, 'beer.details.html', context)
