from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  return HttpResponse("This the start of blogs")

def new(request):
  return HttpResponse('This is blogs new')

def create(request):
  return HttpResponse('This blogs create')

def show(request, number):
  num = number
  return HttpResponse(f'This is blogs {num}')

def edit(request, number):
  return HttpResponse(f'This is the edit page {number}')

def destroy(request, number):
  return HttpResponse(f'This is the delete route{number}')