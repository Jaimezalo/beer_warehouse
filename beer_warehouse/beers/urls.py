from django.conf.urls import url

from views import first_view


urlpatterns = [
    url(r'^$', first_view, name='first-view'),
]
