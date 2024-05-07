from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import *
from .forms import *
import csv
from .importviews import *


def import_cpu(request):
    if request.method == 'POST':
        form = CPUImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                CPU.objects.get_or_create(
                tipo=row[0],
                score=row[2],
                nome=row[1],
                custo=row[3],
                preco=row[4]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = CPUImportForm()

    return render(request, 'import.html', {'form': form})

def import_gpu(request):
    if request.method == 'POST':
        form = GPUImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                GPU.objects.get_or_create(
                tipo=row[0],
                nome=row[1],
                score = row[2],
                custo=row[3],
                preco=row[4]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = GPUImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def import_psu(request):
    if request.method == 'POST':
        form = PSUImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                PSU.objects.get_or_create(
                tipo=row[0],
                nome=row[1],
                custo=row[2],
                preco=row[3]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = PSUImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def import_mob(request):
    if request.method == 'POST':
        form = MOBImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                MOB.objects.get_or_create(
                tipo=row[0],
                nome=row[1],
                custo=row[2],
                preco=row[3]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = MOBImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def import_ram(request):
    if request.method == 'POST':
        form = RAMImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                RAM.objects.get_or_create(
                tipo=row[0],
                nome=row[1],
                custo=row[2],
                preco=row[3]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = RAMImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def import_sto(request):
    if request.method == 'POST':
        form = STOImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                STO.objects.get_or_create(
                tipo=row[0],
                nome=row[1],
                custo=row[2],
                preco=row[3]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = STOImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def import_gab(request):
    if request.method == 'POST':
        form = GABImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data_reader = csv.reader(csv_file.read().decode('utf-8').splitlines())

            for row in data_reader:
                GAB.objects.get_or_create(
                tipo=row[0],
                nome=row[1],
                custo=row[2],
                preco=row[3]
            )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = GABImportForm()

    return render(request, 'import.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')