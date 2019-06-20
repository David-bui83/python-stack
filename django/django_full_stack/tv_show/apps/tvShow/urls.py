from django.conf.urls import url 
from . import views 

urlpatterns = [
  url(r'^$',views.index),
  url(r'^shows$',views.shows),
  url(r'^shows/new$', views.show_new),
  url(r'^shows/create$', views.create_show),
  url(r'^shows/(?P<id>\d+)$',views.display_show),
  url(r'^shows/(?P<id>\d+)/edit$',views.edit_show),
  url(r'^shows/(?P<id>\d+)/make_edit$',views.make_edit),
  url(r'^delete/(?P<id>\d+)',views.delete)
]