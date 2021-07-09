from django.shortcuts import render, redirect
from .models import task
from django.contrib import messages

def signup(request):

    return render(request, 'signup1.html')


def user(request):
    name = request.POST['name1']
    email = request.POST['email1']
    psw = request.POST['psw1']
    task(name = name, password=psw, email=email).save()
    return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def authentication(request):
    if request.method == "POST":
        try:
            username = request.POST['uname']
            password = request.POST['psw']

            obj = task.objects.get(email=username, password=password)
            userid = obj.id

            if task.objects.filter(email=username, password=password):
                return redirect('homepage', userid)


            else:
                messages.success(request, "Username/Password invalid!!!")
                return redirect('login')

        except task.DoesNotExist as e:
            messages.success(request, "Username/Password invalid!!!")
    return render(request, "login.html")


def homepage(request,user):
    obj = task.objects.filter(id=user)
    context = {'obj':obj}

    return render(request, 'homepage.html',context)

def index(request):
    return render(request, 'index.html')

def pale(request):
    return render(request, 'pale.html')



