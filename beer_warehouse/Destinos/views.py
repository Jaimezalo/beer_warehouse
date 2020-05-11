# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from forms import DestinoForm
from models import Destino


class DestinoListView(ListView):
    model = Destino


class DestinoDetailView(DetailView):
    model = Destino


class DestinoUpdateView(UpdateView):
    model = Destino
    form_class = DestinoForm
    success_url = reverse_lazy('destino-list-view')


class DestinoCreateView(CreateView):
    model = Destino
    form_class = DestinoForm
    success_url = reverse_lazy('destino-list-view')

