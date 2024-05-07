from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import *
from .forms import *
from .importviews import *
# Create your views here.

def home(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def partpicker(request):
    return render(request, 'partpicker.html', {
        'CPU': cpuform
    })