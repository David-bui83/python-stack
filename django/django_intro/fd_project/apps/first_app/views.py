from django.shortcuts import render, redirect, HttpResponse 

# Create your views here.
def index(request):
  return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
  return HttpResponse("placeholder to diaplay a new form to create a new blog")

def create(request):
  return redirect('/')

def number(request, number):
  return HttpResponse(f"place holder to display blog number {number}")

def edit(request, id):
  return HttpResponse(f"placeholder to edit blog {id} with a method named 'edit'")

def destroy(request, id):
  return redirect('/')