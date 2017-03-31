from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
    #url(r'logout/^$', views.logout, name='logout'),
    #xo
    #url(r'^xo/$', views.xo, name='xo'),
]
