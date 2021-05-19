from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    if 'bigCounter' not in request.session:
        request.session['bigCounter'] = 1
    elif 'bigCounter' in request.session:
        request.session['bigCounter'] += 1

    if 'counter' not in request.session:
        request.session['counter'] = 1
    elif 'counter' in request.session:
        request.session['counter'] += 1
    return render(request,'index.html')

def destroy(request):
    del request.session['counter']
    return redirect('/')

def plus(request):
    request.session['counter'] += 1
    return redirect('/')

def add(request):
    if request.method == 'POST':
        addValue = int(request.POST['add'])-1
        request.session['counter'] += addValue
        return redirect('/')