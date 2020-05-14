# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView
from forms import DestinoForm
from models import Destino


class DestinoUpdateView(UpdateView):
    model = Destino
    form_class = DestinoForm
    success_url = reverse_lazy('destino-list-view')


class DestinoCreateView(CreateView):
    model = Destino
    form_class = DestinoForm
    success_url = reverse_lazy('destino-list-view')


class DestinoCompania(TemplateView):
    template_name = 'Destinos/compania.html'


class DestinoAfluencia(TemplateView):
    template_name = 'Destinos/afluencia.html'


class DestinoPresupuesto(TemplateView):
    template_name = 'Destinos/presupuesto.html'