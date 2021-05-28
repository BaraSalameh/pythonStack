from django.urls import path
from . import views

urlpatterns = [
    path('wall', views.index),
    path('add_post', views.add_post),
    path('add_comment', views.add_comment),
]