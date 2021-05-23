from django.db import models
from django.db.models.base import Model

# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def showTable():
    return users.objects.all()

def addRow(fn,ln,e,a):
    users.objects.create(first_name = fn, last_name = ln, email_address = e, age = a)
    