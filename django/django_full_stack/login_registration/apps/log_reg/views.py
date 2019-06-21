from django.shortcuts import render, HttpResponse, redirect
from apps.log_reg.models import *
from django.contrib import messages
from datetime import datetime
import bcrypt

# Create your views here.
def index(request):
  return render(request, 'log_reg/index.html')

def register(request):
  errors = User.objects.basic_validator(request.POST)
  exist = User.objects.filter(email=request.POST['email'])
  print(exist)
  if exist:
    messages.error(request, 'Email is unavaliable')
    return redirect('/')
    
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
      return redirect('/')
  else:
    hashed_pass = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hashed_pass)
    success = User.objects.last()
    request.session['user_id'] = success.id
    print(request.session['user_id'])
    return redirect('/success')

def success(request):
  if not 'user_id' in request.session:
    return redirect('/')
  
  context = {
    'user': User.objects.get(id=request.session['user_id'])
  }
  return render(request, 'log_reg/success.html', context)

def login(request):

  try:
    User.objects.get(email=request.POST['lge'])
  except:
    messages.error(request, 'Invalid user')
    return redirect('/')
  user_pw = User.objects.get(email=request.POST['lge'])
  if bcrypt.checkpw(request.POST['login-pw'].encode(), user_pw.password.encode()):
    request.session['user_id'] = user_pw.id
    return redirect('/success')
  else:
    messages.error(request, 'Incorrect password')
    return redirect('/')
  

def delete(request):
  del request.session['user_id']
  return redirect('/')
