from django.core.checks import messages
from django.shortcuts import redirect, render
from . import models
from django.contrib import messages

# Create your views here.

def is_there_any_post():
    return models.get_posts()

def index(request):
    posts = is_there_any_post()
    context = {'posts': posts}
    return render(request, 'wall.html', context)


def post_validation(message):
    return models.post_validation(message)


def comment_validation(comment):
    return models.comment_validation(comment)

def set_message(message , user_id):
    models.set_message(message, user_id)

def set_comment(comment, user_id, message_id):
    models.set_comment(comment, user_id, message_id)


def add_post(request):
    if request.method == 'POST':
        message = request.POST['message']
        post = post_validation(message)
        if len(post) > 0:
            for key, value in post.items():
                messages.error(request, value)
            return redirect('/wall')
        set_message(message, request.session['id'])
    return redirect('/wall')


def add_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        comment_validate = comment_validation(comment)
        if len(comment_validate) > 0:
            for key, value in comment_validate.items():
                messages.error(request, value)
            return redirect('/wall')
        set_comment(comment, request.session['id'], request.POST['message_id'])
    return redirect('/wall')