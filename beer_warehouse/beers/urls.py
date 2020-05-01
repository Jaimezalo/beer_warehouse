from django.conf.urls import url

from views import beer_list_view, beer_detail_view

urlpatterns = [
    url(r'^beer/list/$', beer_list_view, name='beer-list-view'),
    url(r'^beer/detail/(?P<pk>\d+)/$', beer_detail_view, name='beer-detail-view'),
]
