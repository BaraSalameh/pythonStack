from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('books',views.addBook),
    path('books/<book_id>',views.showSpecialBook),
    path('addAuthor/<book_id>',views.addAuthor),
    path('authors', views.author),
    path('addAuthors',views.addAuthor),
    path('authors/<author_id>',views.showSpecialAuthor),
    path('addBook/<author_id>', views.addAuthor),
]