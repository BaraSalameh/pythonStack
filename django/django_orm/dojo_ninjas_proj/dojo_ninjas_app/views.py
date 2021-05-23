from django.shortcuts import redirect, render
from . import models

# Create your views here.

def index(request):
    dojo_id = models.Dojo.get_id()
    dojo_all = models.Dojo.dojo_all()
    ninja_all = models.Ninja.ninja_all()
    context = {
        'dojo_id':dojo_id,
        'dojo_all':dojo_all,
        'ninja_all':ninja_all
    }

    return render(request,'index.html',context)

def dojo_process(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']

        models.Dojo.set_dojo(name,city,state)
    return redirect('/')

def ninjaProcess(request):
    if request.method == 'POST':
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        did = request.POST['dojo_id']

        models.Ninja.set_ninja(fn,ln,did)
    return redirect('/')