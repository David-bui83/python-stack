from django.shortcuts import render, HttpResponse, redirect
from apps.bookAuthorApp.models import *

# Create your views here.
def index(request):
  return render(request, 'book_author/index.html')

def books(request):
  context = {
    'books': Book.objects.all()
  }
  return render(request, 'book_author/books.html', context)

def create_book(request):
  Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
  return redirect('/books')

def view_book(request, id):
  book = Book.objects.get(id=id)

  b_authors = book.authors.all()
  all_authors = Author.objects.all()
  new_author_arr = []
  for author in all_authors:
    if author not in b_authors:
      new_author_arr.append(author)

  context = {
    'book': Book.objects.get(id=id),
    'authors': book.authors.all(),
    'all_authors': new_author_arr
  }

  return render(request, 'book_author/view_book.html', context)

def add_author(request):
  book = Book.objects.get(id=request.POST['book_id'])
  author = Author.objects.get(id=request.POST['author_id'])
  book.authors.add(author)
  return redirect('/view_book/' + str(request.POST['book_id']))

def authors(request):

  context = {
    'authors': Author.objects.all()
  }
  return render(request, 'book_author/authors.html', context)

def create_author(request):
  Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
  return redirect('/authors')

def view_author(request, id):
  author = Author.objects.get(id=id)

  a_books = author.books.all()
  all_books = Book.objects.all()
  new_book_arr = []
  for book in all_books:
    if book not in a_books:
      new_book_arr.append(book)

  context = {
    'author': Author.objects.get(id=id),
    'books': author.books.all(),
    'all_books': new_book_arr
  }

  return render(request, 'book_author/view_author.html', context)

def add_book(request):

  book = Book.objects.get(id=request.POST['book_id'])
  author = Author.objects.get(id=request.POST['author_id'])
  author.books.add(book)

  

  return redirect('view_author/'+ str(request.POST['author_id']))
