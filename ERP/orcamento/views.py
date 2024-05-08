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
        'CpuSelectForm': CpuSelectForm,
        'GpuSelectForm': GpuSelectForm,
        'PSUSelectForm': PSUSelectForm,
        'MobSelectForm': MobSelectForm,
        'RamSelectForm': RamSelectForm,
        'GabSelectForm': GabSelectForm,
        'stoSelectForm': stoSelectForm,
    })

def display_values(request):
    if request.method == 'POST':
        forms = {
            'cpu': CpuSelectForm(request.POST),
            'gpu': GpuSelectForm(request.POST),
            'psu': PSUSelectForm(request.POST),
            'mob': MobSelectForm(request.POST),
            'ram': RamSelectForm(request.POST),
            'gab': GabSelectForm(request.POST),
            'sto': stoSelectForm(request.POST),
        }
        if all(form.is_valid() for form in forms.values()):
            context = {key: form.cleaned_data[key] for key, form in forms.items()}
            return render(request, 'display_values.html', context)

    return render(request, 'partpicker.html')

