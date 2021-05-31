from django.db.models.deletion import CASCADE
from login_app.models import User
from django.db import models

# Create your models here.

class ThoughtManager(models.Manager):
    def basic_validator(self, thought):
        errors = {}
        if len(thought) < 5:
            errors['thought'] = "The thought must be at least 5 characters"
        return errors

class Thought(models.Model):
    thought = models.TextField()
    user_id = models.ForeignKey(User, related_name='thoughts', on_delete=CASCADE)
    likes = models.ManyToManyField(User, related_name='thought_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ThoughtManager()


def get_thoughts():
    return Thought.objects.all()

def set_thought(thought, user):
    Thought.objects.create(thought = thought, user_id = user)

def validate_thought(thought):
    return Thought.objects.basic_validator(thought)

def delete_thought(thought_id):
    thought = Thought.objects.get(id = thought_id)
    thought.delete()

def get_thought(thought_id):
    return Thought.objects.get(id = thought_id)

def set_like(thought, user):
    thought.likes.add(user)

def dislike(thought, user):
    thought.likes.remove(user)
