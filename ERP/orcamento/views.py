from django.shortcuts import render
from django.http import request
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def partpicker(request):
    return render(request, 'partpicker.html', {
        'cpuform': cpuform,
         "CPU": CPU,
    })
