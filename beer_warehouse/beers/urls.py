from django.conf.urls import url

from views import beer_detail_view, BeerListView, beer_list_view

urlpatterns = [
    url(r'^beer/list/$', beer_list_view, name='beer-list-view'),
    url(r'^beer/detail/(?P<pk>\d+)/$', beer_detail_view, name='beer-detail-view'),
    # url(r'^beer/list/$', BeerListView.as_view, name='beer-list-view'),
]
