from django.http import request
from django.shortcuts import redirect, render
from . import models

# Create your views here.

# A method to handle '/' route and goes to '/shows'
def index(request):
    return redirect('/shows')


# A method to handle '/shows' to render 'index.html'
def showReadAll(request):
    context = {'tvShows': models.getAll()}

    return render(request,'index.html',context)

# A method to handle '/shows/new' from index.html anchor to render 'create.html'
def addANewShow(request):
    return render(request,'create.html')

# A method to handle '/shows/setTvShow' from create.html form to add a new row to database
# and return that row id, then redirect to '/shows/<int:tvShowId>'
def setTvShow(requset):
    if requset.method == "POST":
        title = requset.POST['title']
        network = requset.POST['network']
        releaseDate = requset.POST['release_date']
        description = requset.POST['description']

        tvShowId = models.setTvShow(title, network, release_date=releaseDate, description=description)

        return redirect('/shows/'+str(tvShowId))
    return redirect('/shows/new')


# A method to handle '/shows/<int:tvShowId>' from setTvShow method or index.html show anchor
# to render 'readOne.html'
def showReadOne(requset, tvShowId):
    context = {'tvShow': models.getTvShow(tvShowId)}

    return render(requset, 'readOne.html', context)


# A method to handle '/shows/<int:tvShowId>/destroy' from create.html delete anchor
# and readOne.html delete anchor to delete
# a special tv show from the database, then redirect to the same page '/shows'
def deleteShowId(request, tvShowId):
    models.deleteTvShow(tvShowId)
    return redirect('/')

# A method to handle '/shows/<int:tvShowId>/edit' from index.html edit anchor 
# and readOne.html edit anchor to get the 
# needed row to edit from the database
# using the passed tvShowId, then render the update.html passing the row id inside context
# in order to show the previous data from the database inside the form
def editShowId(request, tvShowId):
    context = {'tvShow':models.getTvShow(tvShowId)}
    return render(request, 'update.html', context)


# A method to handle '/updateTvShow/<int:tvShowId>' from update.html form to update the row inside the database
# then redirect to '/shows/<int:tvShowId>'
def updateTvShow(request, tvShowId):
    if request.method == "POST":
        title = request.POST['title']
        network = request.POST['network']
        releaseDate = request.POST['release_date']
        description = request.POST['description']

        models.updateTvShow(tvShowId, title, network, releaseDate, description)

        return redirect('/shows/'+str(tvShowId))
    return redirect('/shows/'+str(tvShowId)+'/edit')

