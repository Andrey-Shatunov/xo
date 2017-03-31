from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #xo
    url(r'^xo/(?P<room_id>[0-9]+)$', views.xo, name='xo'),
]
