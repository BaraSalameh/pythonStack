from django.db import models
import re


# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not post_data['first_name'].isalpha() or len(post_data['first_name']) < 2:
            errors['first_name'] = "First name you provided is not all alphabets or it's less than 2 characters"
        if not post_data['last_name'].isalpha() or len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name you provided is not all alphabets or it's less than 2 characters"
        if not email_regex.match(post_data['email']):
            errors['email'] = "The email address is not valid"
        if len(post_data['password']) < 8:
            errors['password'] = "password should be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "The passwords doesn't match"
        return errors
    def login_validator(self, post_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "The email address is not valid"
        if len(post_data['password']) < 8:
            errors['password'] = "password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    


def register_validation(post_data):
    return User.objects.basic_validator(post_data)


def login_validation(post_data):
    return User.objects.login_validator(post_data)



def create_user(first_name, last_name, email, password):
    User.objects.create(first_name = first_name, last_name = last_name, email = email, password = password)
    new_user = User.objects.last()
    return new_user


def get_user(email,password):
    users = User.objects.filter(email = email, password = password)
    if len(users) > 0:
        return users[0]
    return None


def retrieve_all_users():
    return User.objects.all()


