from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create_dojo',views.dojo_process),
    path('create_ninja',views.ninjaProcess)
]