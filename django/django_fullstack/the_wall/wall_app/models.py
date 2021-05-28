from django.core.checks.messages import Error
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.manager import Manager
from login_app.models import User
# Create your models here.

class MessageManager(models.Manager):
    def basic_validator(self, message):
        errors = {}
        if len(message) < 1:
            errors['message'] = "you can't add an empty Message"
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, comment):
        errors = {}
        if len(comment) < 1:
            errors['comment'] = "you can't add an empty Comment"
        return errors

class Message(models.Model):
    message = models.TextField()
    user_id = models.ForeignKey(User, related_name= 'user_messages', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()


class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User, related_name= 'user_comments', on_delete=CASCADE)
    message_id = models.ForeignKey(Message, related_name= 'post_comments', on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()


def get_posts():
    return Message.objects.all().order_by('-updated_at')

def post_validation(message):
    return Message.objects.basic_validator(message)


def comment_validation(comment):
    return Comment.objects.basic_validator(comment)

def set_message(message, user_id):
    user = User.objects.get(id = user_id)
    Message.objects.create(message = message, user_id = user)

def set_comment(comment, user_id, message_id):
    user = User.objects.get(id = user_id)
    message = Message.objects.get(id = message_id)
    Comment.objects.create(comment = comment, user_id = user, message_id = message)