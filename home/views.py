from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')