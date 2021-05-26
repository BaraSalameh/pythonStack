from django.core.checks import messages
from django.db.models.expressions import Value
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from . import models

# Create your views here.

# A method to handle '/' route and goes to '/shows'
def index(request):
    return redirect('/shows')


# A method to handle '/shows' to render 'index.html'
def showReadAll(request):
    context = {'tvShows': models.getAll()}
    print(f"context content:{context['tvShows']}")
    return render(request,'index.html',context)

# A method to handle '/shows/new' from index.html anchor to render 'create.html'
def addANewShow(request):
    return render(request,'create.html')


# A function that handle setTvShow method call to contact with the models method witch validate the data
def validate_set_tv_show(posted_data):
    return models.validate_set_tv_show(posted_data)

# A function that handle setTvShow method call to contact with the models witch validate the title
def validate_title(title):
    return models.validate_title(title)

# A method to handle '/shows/setTvShow' from create.html form to add a new row to database
# and return that row id, then redirect to '/shows/<int:tvShowId>'
def setTvShow(requset):
    if requset.method == "POST":
        title = requset.POST['title']
        network = requset.POST['network']
        releaseDate = requset.POST['release_date']
        description = requset.POST['description']

        errors = validate_set_tv_show(requset.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(requset, value)
            return redirect('/shows/new')
        
        title_erorrs = validate_title(requset.POST['title'])
        if len(title_erorrs) > 0:
            for key, value in title_erorrs.items():
                messages.error(requset, value)
            return redirect('/shows/new')

        tvShowId = models.setTvShow(title, network, release_date=releaseDate, description=description)
        messages.success(requset, "Tv Show successfully added")
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

        errors = validate_set_tv_show(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/'+str(tvShowId)+'/edit')
        else:
            models.updateTvShow(tvShowId, title, network, releaseDate, description)
            messages.success(request, "row updated successfully")
            return redirect('/shows/'+str(tvShowId))
    return redirect('/shows/'+str(tvShowId)+'/edit')

