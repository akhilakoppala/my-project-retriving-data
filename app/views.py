from django.shortcuts import render
from app.models import *

# Create your views here.

def display_topic(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QST=Webpage.objects.all()
    d={'webpages':QST}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QST=AccessRecords.objects.all()
    d={'accessrecords':QST}
    return render(request,'display_access.html',d)
