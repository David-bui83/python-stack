from django.conf.urls import url 
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^register$', views.register),
  url(r'^success$', views.success),
  url(r'^delete$', views.delete),
  url(r'^login$', views.login)
]