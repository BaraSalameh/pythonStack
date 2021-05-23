from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from users_app import models

# Create your views here.

def index(request):
    newTable = models.showTable()
    
    context = {
        "showTable" : newTable
    }
    print(newTable[0].first_name)
    return render(request,'index.html',context)

def process(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email_address']
        age = request.POST['age']
    models.addRow(first_name,last_name,email_address,age)

    return redirect('/')