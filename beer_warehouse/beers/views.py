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

from forms import CompanyForm
from models import Beer, Company


class BeerListView(ListView):
    model = Beer


class BeerDetailView(DetailView):
    model = Beer


class CompanyListView(ListView):
    model = Company


# def company_edit_view(request, pk):
#     company = get_object_or_404(Company, pk=pk)
#
#     if request.method == 'GET':
#         form = CompanyForm(instance=company)
#     else:
#         form = CompanyForm(request.POST, instance=company)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'company': company,
#         'form': form
#     }
#
#     return render(request, 'company/company_form.html', context)


class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list-view')


class CompanyDetailView(DetailView):
    model = Company
