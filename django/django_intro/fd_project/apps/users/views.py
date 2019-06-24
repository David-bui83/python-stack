from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  return HttpResponse('Index for users registration')
def register(request):
  return HttpResponse('Placeholder for users to creae a new user record')

def login(request):
  return HttpResponse('Placeholder for users to log in')

def new(request):
  return HttpResponse('Placeholder for new users')

def users(request):
  return HttpResponse('Placeholder to later display all the list of users')
