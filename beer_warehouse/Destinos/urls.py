from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from views import DestinoUpdateView, DestinoCreateView, DestinoCompania, DestinoAfluencia, DestinoPresupuesto

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^destino/compania/$', DestinoCompania.as_view(), name='compania'),
    url(r'^destino/afluencia/(\d+)/$', DestinoAfluencia.as_view(), name='afluencia'),
    url(r'^destino/compania/$', DestinoPresupuesto.as_view(), name='presupuesto'),


    url(r'^destino/edit/(?P<pk>\d+)/$', login_required(DestinoUpdateView.as_view()), name='destino-edit-view'),
    url(r'^destino/create/$', login_required(DestinoCreateView.as_view()), name='destino-create-view'),

]
