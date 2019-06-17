from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 

# Create your views here.
def index(request):
  context = {
    'time': strftime("%Y-%m-%d %H:%M %p", gmtime()),
    'new_time': strftime("%B-%d-%y %H:%M %p", gmtime()),
  }
  return render(request, 'display_time/index.html', context)