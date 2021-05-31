from django.urls import path
from . import views

urlpatterns = [
    path('thoughts', views.thoughts),
    path('add_thought', views.add_thought),
    path('delete', views.delete_thought),
    path('thoughts/<thought_id>', views.thought_boord),
    path('like', views.like),
    path('unlike', views.unlike),
]