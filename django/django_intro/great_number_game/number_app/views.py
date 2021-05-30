from django.shortcuts import redirect, render
import random
# Create your views here.

def index(request):
    if 'my_number' not in request.session:
        request.session['my_number'] = 50 #random.randint(1,101)
    print("my number :",request.session['my_number'])
    return render(request,'index.html')

def check(request):
    if request.method == 'POST':
        guessed_number = request.POST['number']
        print("guessed number :",guessed_number)
        request.session['winner'] = 0
        request.session['too_low'] = 0
        request.session['too_high'] = 0
        if request.session['my_number'] == int(guessed_number):
            request.session['winner'] = 1
        elif request.session['my_number'] > int(guessed_number):
            request.session['too_low'] = 1
        elif request.session['my_number'] < int(guessed_number):
            request.session['too_high'] = 1
    return redirect('/show')
        
def show(request):
    context = {
        "winner" : request.session['winner'],
        "too_low" : request.session['too_low'],
        "too_high" : request.session['too_high'],
    }
    return render(request,'index.html',context)
    
def play_again(request):
    request.session.clear()
    return redirect('/')