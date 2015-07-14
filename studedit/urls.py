__author__ = 'oqqrez'

from django.conf.urls import include, url
from studedit import views

urlpatterns = [
    url(r'^(?P<sender_id>[0-9]+)/$', views.show_list),
    url(r'^(?P<sender_id>[0-9]+)/add/$', views.add),
    url(r'^(?P<sender_id>[0-9]+)/add/ok/$', views.add_ok)
]
