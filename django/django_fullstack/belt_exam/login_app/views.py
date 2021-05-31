from sre_constants import error
from django.core.checks import messages
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
import re
from thoughts_app import models
from . import models

# Create your views here.

def index(request):
    """
    Description: The main method, it handles '/' route
    Return: render 'index.html', send all the users by the context to the template
    """
    return render(request,'index.html')




def register_validation(post_data):
    """
    Description: a function that handles views.register method call to validate the first
        form from 'index.html' by sending the information to the models.register_validation
    Parametres: 
        post_data -> the information in the form post
    Return: the result of the validation proccess, whether the user registred successfully or not.
    """ 
    return models.register_validation(post_data)



def login_validation(post_data):
    """
    Description: a function that handles views.login method call to validate the second
        form from 'index.html' by sending the information to the models.login_validation
    Parametres: 
        post_data -> the information in the form post
    Return: the result of the validation proccess, whether the user logged in successfully or not.
    """ 
    return models.login_validation(post_data)


    

def register(request):
    """
    Description: method handles '/register' route from index.html first form in order to recive the user
        registration information
    Return: redirect '/thoughts' if the information are valid
        redirect '/' if the information aren't valid
    """
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        validated = register_validation(request.POST)
        if len(validated) > 0:
            for key, value in validated.items():
                messages.error(request, value)
            return redirect('/')
        request.session['first_name'] = first_name
        user = models.create_user(first_name,last_name,email,password)
        registered_user = models.get_last_user()
        request.session['id'] = registered_user.id
        return redirect('/thoughts')
    return redirect('/')




def login(request):
    """
    Description: method handles '/login' route to get data from second form from 'index.html'
        in order to validate data and let the user to login
    Return: redirect to '/thoughts' route to view thoughts.html
        redirect to '/' if something wrong happend
    """
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = models.get_user(email, password)
        check_login = login_validation(request.POST)
        if len(check_login) > 0:
            for key, Value in check_login.items():
                messages.error(request, Value)
            return redirect('/')
        if user:
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect('/thoughts')
        messages.error(request, 'wrong email or password')
    return redirect('/')




def logout(request):
    """
    Description: method handles '/logout' route from 'welcome.html' to clear the session values
    Return: redirect the the main page '/'
    """
    request.session.clear()
    return redirect('/')



