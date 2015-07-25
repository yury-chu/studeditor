__author__ = 'oqqrez'

from django.conf.urls import include, url
from studedit import views

urlpatterns = [
    url(r'^$', views.show_list),
    url(r'^add/$', views.add),
    url(r'^add/ok/$', views.add_ok)
]
