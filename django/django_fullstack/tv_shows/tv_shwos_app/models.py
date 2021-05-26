from django.contrib.messages.api import error
from django.db import models

# Create your models here.

class TvShowManager(models.Manager):
    def basic_validation(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = 'The Title field should be at least 2 characters'
        if len(post_data['network']) < 3:
            errors['network'] = 'The Network field should be at least 3 characters'
        if len(post_data['description']) < 10:
            errors['description'] = 'The Description text area should be at least 10 characters'
        return errors
    
    def validate_title(self, title, titles):
        title_errors = {}
        for table_title in titles:
            if table_title.title == title:
                title_errors['unique_title'] = 'The title you provided is already exists!'
        return title_errors


class TvShows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(default="01-01-2010")
    description = models.TextField(default="No description added")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvShowManager()

def getAll():
    return TvShows.objects.all()

def validate_title(title):
    titles = TvShows.objects.all()
    return TvShows.objects.validate_title(title, titles)
    

def validate_set_tv_show(post_data):
    return TvShows.objects.basic_validation(post_data)


def setTvShow(title,network,release_date = "01-01-2010", description = "No description added"):
    TvShows.objects.create(title = title, network = network, release_date = release_date, description = description)
    lastTvShow = TvShows.objects.last()
    return lastTvShow.id

def getTvShow(id):
    return TvShows.objects.get(id = id)

def deleteTvShow(id):
    tvShow = TvShows.objects.get(id = id)
    tvShow.delete()

def updateTvShow(id,title,network,release_date,description):
    tvShow = TvShows.objects.get(id = id)
    tvShow.title = title
    tvShow.network = network
    tvShow.release_date = release_date
    tvShow.description = description
    tvShow.save()
