from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('check',views.check),
    path('play_again', views.play_again),
    path('show', views.show)
]