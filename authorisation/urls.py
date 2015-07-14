__author__ = 'oqqrez'

from django.conf.urls import include, url
from authorisation import views

urlpatterns = [
    url(r'^who/$', views.who),
    url(r'^sender/(?P<sender_id>[0-9]+)/$', views.is_sender),

]
