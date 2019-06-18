from django.shortcuts import render, HttpResponse, redirect 
import random
from datetime import datetime

# Create your views here.
def index(request):
  return render(request, 'index.html')

def process_money(request):
  if not 'gold' in request.session:
    request.session['gold'] = 0 
  if not 'act_out' in request.session:
    request.session['act_out'] = []

  print(request.POST['name'])

  building = {
    'farm': (10,20),
    'cave': (5,10),
    'house': (2,5),
    'casino': (-50,50)
  }
  
  gold = random.randint(building[request.POST['name']][0], building[request.POST['name']][1])
  now = datetime.time(datetime.now())

  if gold < 0:
    str_out = f"<p class='red'>Entered a {request.POST['name']} and lost {gold}! ({now})</p>"
    request.session['gold'] -= gold
  else:
    str_out = f"<p class='green'>Earned {gold} golds from the {request.POST['name']}! ({now}) </p>"
    request.session['gold'] += gold  
  print(gold)

  request.session['act_out'].append(str_out)
  print(request.session['act_out'])
  return redirect('/')

def reset(request):
  del request.session['gold']
  del request.session['act_out']
  return redirect('/')