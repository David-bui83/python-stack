from django.shortcuts import render, HttpResponse, redirect
from apps.tvShow.models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
  return render(request, 'tvShow/index.html')

def shows(request):
  context = {
    'shows': Show.objects.all()
  }
  return render(request, 'tvShow/shows.html', context)

def show_new(request):
  
  return render(request, 'tvShow/show_new.html')

def create_show(request):

  errors = Show.objects.basic_validator(request.POST)
  # print(request.POST['date'])
  # print(datetime.strptime(request.POST['date'], '%Y-%m-%d'))
  exist = Show.objects.filter(title=request.POST['title'])
  if exist:

    messages.error(request, 'Show already in database')
    return redirect('/shows/new')
  else:
    if len(errors) > 0:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('/shows/new')
  
    new_show = Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['date'],desc=request.POST['desc'])

    return redirect('/shows/' + str(new_show.id))

def display_show(request, id):
  context= {
    'show': Show.objects.get(id=id)
  } 
  return render(request, 'tvShow/display_show.html', context)

def edit_show(request, id):
  context= {
    'show': Show.objects.get(id=id),
  
  } 
  return render(request, 'tvShow/edit.html', context)

def make_edit(request, id):

  errors = Show.objects.basic_validator(request.POST)
  
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/shows/'+ str(id)+'/edit')
  else:

    edit_show = Show.objects.get(id=id)

    edit_show.title = request.POST['title']
    edit_show.network = request.POST['network']
    edit_show.release_date = request.POST['date']
    edit_show.desc = request.POST['desc']
    edit_show.save()

  return redirect('/shows/'+ str(id))

def delete(request, id):
  del_show = Show.objects.get(id=id)
  del_show.delete()
  return redirect('/shows')