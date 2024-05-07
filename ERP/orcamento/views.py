from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import *
from .forms import *
import csv

# Create your views here.

def home(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def partpicker(request):
    return render(request, 'partpicker.html', {
        'CPU': cpuform
    })

def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                PCPART.objects.create(
                tipo=['tipo'],
                nome=['nome'],
                custo=['custo'],
                preco=['preco']
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = CSVImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')
