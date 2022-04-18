from datetime import datetime

from django.shortcuts import render

# Create your views here.
from inv.models import Item


def index(request):
    date = datetime.today()
    items = Item.objects.all()
    return render(request, "inv/index.html", context={'date': date, 'items':items})

def home(request):
    date = datetime.today()
    return render(request, "inv/home.html", context={'date':date,})

def show(request):
    items = Item.objects.all()
    return render(request, "inv/show.html", context={'items': items})

def add(request):
    items = Item.objects.all()
    return render(request, "inv/add.html", context={'items': items})