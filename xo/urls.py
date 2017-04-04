from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
url(r'^xo/(?P<room_id>[0-9]+)/add_win$', views.add_win, name='add_win'),
    #xo
    url(r'^xo/(?P<room_id>[0-9]+)$', views.xo, name='xo'),
    url(r'^xo/check_full_room/(?P<room_id>[0-9]+)$', views.check_full_room, name='check_full_room'),
    #win
    url(r'^add_win$', views.add_win, name='add_win'),
]
