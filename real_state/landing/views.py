from django.shortcuts import render

from .models import Properties

# Create your views here.

def home(request):
    return render(request, "index.html", {'property': Properties.objects.all()})

