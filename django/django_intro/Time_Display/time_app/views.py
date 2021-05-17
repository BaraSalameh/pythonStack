from django.shortcuts import render
from time import strftime , gmtime

# Create your views here.

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M")
    }
    return render(request,'index.html', context)