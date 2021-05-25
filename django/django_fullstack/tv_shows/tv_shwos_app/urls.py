from django.urls import path
from . import views, models

urlpatterns = [
    path('',views.index),
    path('shows',views.showReadAll),
    path('shows/new',views.addANewShow),
    path('shows/setTvShow', views.setTvShow),
    path('shows/<int:tvShowId>', views.showReadOne),
    path('shows/<int:tvShowId>/destroy', views.deleteShowId),
    path('shows/<int:tvShowId>/edit', views.editShowId),
    path('updateTvShow/<int:tvShowId>', views.updateTvShow),
]