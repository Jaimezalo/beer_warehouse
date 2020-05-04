from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from forms import CompanyForm
from views import BeerListView, BeerDetailView, CompanyListView, CompanyUpdateView, CompanyDetailView, CompanyCreateView

urlpatterns = [
    url(r'^beer/list/$', login_required(BeerListView.as_view()), name='beer-list-view'),
    url(r'^beer/detail/(?P<pk>\d+)/$', login_required(BeerDetailView.as_view()), name='beer-detail-view'),

    url(r'^company/list/$', login_required(CompanyListView.as_view()), name='company-list-view'),
    url(r'^company/edit/(?P<pk>\d+)/$', CompanyUpdateView.as_view(), name='company-edit-view'),
    url(r'^company/create/$', CompanyCreateView.as_view(), name='company-create-view'),
    url(r'^company/detail/(?P<pk>\d+)/$', CompanyDetailView.as_view(), name='company-detail-view'),
]
