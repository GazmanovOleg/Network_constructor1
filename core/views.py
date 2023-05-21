from django.http import HttpResponse
from django.shortcuts import render
from .models import Router


def index(request):
    routers = Router.objects.all()

    return render(request, "index.html", {"routers":routers})