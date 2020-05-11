from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from views import DestinoListView, DestinoDetailView, DestinoUpdateView, DestinoCreateView

urlpatterns = [
    url(r'^destino/list/$', DestinoListView.as_view(), name='destino-list-view'),
    url(r'^destino/detail/(?P<pk>\d+)/$', DestinoDetailView.as_view(), name='destino-detail-view'),
    url(r'^destino/edit/(?P<pk>\d+)/$', DestinoUpdateView.as_view(), name='destino-edit-view'),
    url(r'^destino/create/$', DestinoCreateView.as_view(), name='destino-create-view'),

]
