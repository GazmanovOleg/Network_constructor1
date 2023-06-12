from django.http import HttpResponse
from django.shortcuts import render
from .models import Router
from django.contrib.auth.models import User


def index(request):
    routers = Router.objects.all()

    return render(request, "index.html", {"routers":routers})




def login(request):
    if request.method == "POST":
        email = request.post.get("e-mail")
        password = request.post.get("password")
        if User.is_superuser(email=email):
            print("Круто")


    return render(request, "login.html")
