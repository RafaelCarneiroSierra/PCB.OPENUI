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
        'CPU': CPU,
    })

def display_values(request):
    if request.method == 'POST':
        cpu_form = CpuSelectForm(request.POST)
        gpu_form = GpuSelectForm(request.POST)
        psu_form = PSUSelectForm(request.POST)
        mob_form = MobSelectForm(request.POST)
        ram_form = RamSelectForm(request.POST)
        gab_form = GabSelectForm(request.POST)
        sto_form = stoSelectForm(request.POST)
        
        if cpu_form.is_valid() and gpu_form.is_valid() and psu_form.is_valid() and mob_form.is_valid() and ram_form.is_valid() and gab_form.is_valid() and sto_form.is_valid():
            # Process the form data and pass it to the template for display
            context = {
                'cpu_data': cpu_form.cleaned_data['cpu'],
                'gpu_data': gpu_form.cleaned_data['gpu'],
                'psu_data': psu_form.cleaned_data['psu'],
                'mob_data': mob_form.cleaned_data['mob'],
                'ram_data': ram_form.cleaned_data['ram'],
                'gab_data': gab_form.cleaned_data['gab'],
                'sto_data': sto_form.cleaned_data['sto'],
            }
            return render(request, 'display_values.html', context)
    
    return render(request, 'partpicker.html')