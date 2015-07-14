__author__ = 'oqqrez'
from django.conf.urls import include, url
from groupedit import views

urlpatterns = [
    url(r'^show/$', views.show),
    url(r'^add/$', views.add),
    url(r'^add/ok/$', views.add_ok),

]
