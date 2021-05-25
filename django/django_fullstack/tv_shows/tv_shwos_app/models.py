from django.db import models

# Create your models here.

class TvShows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(default="01-01-2010")
    description = models.TextField(default="No description added")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def getAll():
    return TvShows.objects.all()

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
