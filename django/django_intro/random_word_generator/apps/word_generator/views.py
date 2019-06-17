from django.shortcuts import render, HttpResponse, redirect 
from django.utils.crypto import get_random_string
# Create your views here.
def index(request): 
  
  return render(request, 'word_generator/index.html')

def random_word(request):
  if 'counter' in request.session:
    request.session['counter'] += 1
  else: 
    request.session['counter'] = 1

  request.session['random_string'] = get_random_string(length=14)
  

  return redirect('/')

def delete(request):
  del request.session['counter']
  del request.session['random_string']
  return redirect('/')
  