from django.urls import path
from . import views
from thoughts_app import urls
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
]