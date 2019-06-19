from django.conf.urls import url 
from . import views 

urlpatterns = [
  url(r'^$', views.index),
  url(r'^books$', views.books),
  url(r'^create_book$', views.create_book),
  url(r'^view_book/(?P<id>\d+)$', views.view_book),
  url(r'^add_author$', views.add_author),
  url(r'^authors$', views.authors),
  url(r'^create_author$', views.create_author),
  url(r'^view_author/(?P<id>\d+)$', views.view_author),
  url(r'^add_book$', views.add_book)
]