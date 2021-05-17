from django.http.response import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.urls.conf import path

# Create your views here.

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect("/blogs")

def createJason():
    js = {"title":"My first blog","content":"Loerm, ipsum dolor sit amet consectetur adipisicing elit."}
    return js

def js(request):
    js = createJason()
    return JsonResponse(js)

