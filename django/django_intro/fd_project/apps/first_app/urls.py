from django.conf.urls import url
from . import views 

urlpatterns = [
  url(r'^$', views.index),
  url(r'^new$', views.new),
  url(r'^create$', views.create),
  url(r'^(?P<number>\d+)$', views.number),
  url(r'^(?P<id>\d+)/edit$',views.edit),
  url(r'^(?P<id>\d+)/delete$', views.destroy)
]