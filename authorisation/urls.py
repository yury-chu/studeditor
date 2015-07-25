#coding:utf-8
__author__ = 'oqqrez'

from django.conf.urls import include, url
from authorisation import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^logout/$', views.logout),
    url(r'^who/$', views.who),
    url(r'^sender/(?P<sender_id>[0-9]+)/$', views.is_sender),
    url(r'^action/', views.action),

]
