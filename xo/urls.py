from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #xo
    url(r'^xo/$', views.xo, name='xo'),
]
