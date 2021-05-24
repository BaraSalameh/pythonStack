from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . import models
# Create your views here.

def index(request):
    context = {
        "books": models.retrieve_books()
    }
    return render(request,'index.html',context)

def addBook(request):
    if request.method == "POST":
        request.session['title'] = request.POST['title']
        request.session['desc'] = request.POST['desc']

        models.setBook(request.session['title'],request.session['desc'])
    return redirect('/')

def showSpecialBook(request,book_id):

    context = {
        "specialBooks": models.retrieveSpecialBook(book_id),
        "authors": models.retrieveAuthors()
    }

    return render(request,'specialBook.html',context)

def addAuthor(request,book_id):
    author = request.POST['authors']
    booki = models.setSpecialAuthor(author,book_id)
    
    return redirect('/books/'+str(booki))

def author(request):
    context = {
        "authors": models.retrieveAuthors()
    }
    return render(request,'authors.html',context)

def addNewAuthor(request):
    if request.method == "POST":
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['notes'] = request.POST['notes']

        models.setAuthor(request.session['first_name'], request.session['last_name'], request.session['notes'])
    return redirect('/authors')

def showSpecialAuthor(request, author_id):
    context = {
        "author": models.retrieveSpecialAuthor(author_id),
        "books" : models.retrieve_books(),
    }
    
    return render(request, 'specialAuthor.html', context)

def addAuthor(request,author_id):
    book = request.POST['authors']

    authi = models.setSpecialBook(book, author_id)
    return redirect('/authors/'+str(authi))