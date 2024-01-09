from django.shortcuts import render
from . import models
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "home.html")

def info(request):
    return render(request, "WhoAreWe.html")

def registerd(request):
    return render(request, "registerd.html")

def login_view(request):
    if request.method == "POST" and 'register' in request.POST:
        name = request.POST["name"]
        mail = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return render(request, "home.html")
        
        else:
            user = models.Profile.objects.create_user(email=mail, user_name=name, password=password1)
            user.save()
            return render(request, "registerd.html")
        
    elif request.method =="POST" and 'login' in request.POST:
        mail = request.POST["email1"]
        password3 = request.POST["password3"]
        user = authenticate(request, email=mail, password=password3)

        if user is not None:
            login(request, user)
            return render(request, "home.html")
        else:
            return render(request, "registerd.html")
        
    return render(request, "login_view.html")