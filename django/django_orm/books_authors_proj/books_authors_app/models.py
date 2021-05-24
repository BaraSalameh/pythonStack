from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    book_id = models.ManyToManyField(Book,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def retrieve_books():
    return Book.objects.all()

def setBook(title,desc):
    Book.objects.create(title = title, desc = desc)

def retrieveSpecialBook(id):
    return Book.objects.get(id = id)

def retrieveAuthors():
    return Author.objects.all()

def setSpecialAuthor(id, book_id):
    author = Author.objects.get(id = id)
    book = Book.objects.get(id = book_id)
    book.authors.add(author)
    return book.id
    
def retrieve_authors():
    return Author.objects.all()

def setAuthor(first_name, last_name, notes):
    Author.objects.create(first_name = first_name, last_name = last_name, notes = notes)

def retrieveSpecialAuthor(id):
    return Author.objects.get(id = id)


def setSpecialBook(id, author_id):
    specialAuthor = Author.objects.get(id = author_id)
    specialBook = Book.objects.get(id = id)

    specialBook.authors.add(specialAuthor)
    return author_id
