from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from login_app import models
import login_app
from . import models
from login_app import models
from django.contrib import messages

import thoughts_app
# Create your views here.

def get_user(user_id):
    return login_app.models.get_user_by_id(user_id)

def get_thoughts():
    return thoughts_app.models.get_thoughts()



def thoughts(request):
    context = {
        'user': get_user(request.session['id']),
        'thoughts': get_thoughts(),
    }
    return render(request, 'thoughts.html', context)

def validate_thought(thought):
    return thoughts_app.models.validate_thought(thought)

def set_thought(thought, user):
    thoughts_app.models.set_thought(thought, user)

def add_thought(request):
    if request.method == 'POST':
        thought = request.POST['thought']
        thought_validation = validate_thought(thought)
        if len(thought_validation) > 0:
            for key, value in thought_validation.items():
                messages.error(request, value)
            return redirect('/thoughts')
        user = get_user(request.session['id'])
        set_thought(thought, user)
    return redirect('/thoughts')


def delete_thought_from_table(thought_id):
    thoughts_app.models.delete_thought(thought_id)

def delete_thought(request):
    if request.method == 'POST':
        thought_id = request.POST['thought_id']
        delete_thought_from_table(thought_id)
    return redirect('/thoughts')


def get_thought(thought_id):
    return thoughts_app.models.get_thought(thought_id)

def get_likes(thought_id):
    return thoughts_app.models.get_likes(thought_id)

def thought_boord(request, thought_id):
    thought = get_thought(thought_id)
    users = thought.likes.all()
    context = {
        'thought': thought,
        'users':users
    }
    return render(request, 'thought_boord.html', context)

def like(request):
    if request.method == 'POST':
        thought_id = request.POST['thought_id']
        user = login_app.models.get_user_by_id(request.session['id'])
        thought = thoughts_app.models.get_thought(thought_id)
        thoughts_app.models.set_like(thought, user)
    return redirect('/thoughts/'+str(thought_id))

def unlike(request):
    if request.method == 'POST':
        thought_id = request.POST['thought_id']
        thought = thoughts_app.models.get_thought(thought_id)
        user = login_app.models.get_user_by_id(request.session['id'])
        thoughts_app.models.dislike(thought, user)
    return redirect('/thoughts/'+str(thought_id))
        