from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def newHtmlPage(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['passwd']
        favLanguage = request.POST['fl']
        gender = request.POST['gender']

        print(email)
        print(password)

        if 'check' in request.POST:
            print('Checked')
            checkBox = 'Checked'
        elif 'check' not in request.POST:
            checkBox = 'Not Checked'

        if gender == '1':
            gender = "Male"
        elif gender == '2':
            gender = "Female"

        print(favLanguage)
        print(gender)

        context = {
            "email":email,
            "password":password,
            "checkBox":checkBox,
            "favLanguage":favLanguage,
            "gender":gender
        }

    return render(request,'newHtml.html',context)