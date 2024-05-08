from django import forms
from .models import *

# This class is a form for selecting parts for an order
# It uses Django's ModelChoiceField to get a list of available parts
# from the database and display it in a drop-down menu
# The queryset parameter is used to narrow the list of parts
# that are displayed in the drop-down menu
# The values_list parameter is used to specify which fields from the
# Part model are included in the list of parts
# The flat parameter is used to flatten the list of tuples
# that is returned by values_list into a simple list of strings
class partSelectForm(forms.Form):
    # Field for selecting the CPU
    # Queryset is a list of all CPUs in the database
    # Label is the text displayed above the drop-down menu
    cpu = forms.ModelChoiceField(
        queryset=CPU.objects.values_list('nome', flat=True), 
        label='CPU'
    )

    # Field for selecting the GPU
    # Queryset is a list of all GPUs in the database
    # Label is the text displayed above the drop-down menu
    gpu = forms.ModelChoiceField(
        queryset=GPU.objects.values_list('nome', flat=True), 
        label='GPU'
    )

    # Field for selecting the PSU
    # Queryset is a list of all PSUs in the database
    # Label is the text displayed above the drop-down menu
    psu = forms.ModelChoiceField(
        queryset=PSU.objects.values_list('nome', flat=True), 
        label='PSU'
    )

    # Field for selecting the RAM
    # Queryset is a list of all RAMs in the database
    # Label is the text displayed above the drop-down menu
    ram = forms.ModelChoiceField(
        queryset=RAM.objects.values_list('nome', flat=True), 
        label='RAM'
    )

    # Field for selecting the MOBO
    # Queryset is a list of all MOBOs in the database
    # Label is the text displayed above the drop-down menu
    mob = forms.ModelChoiceField(
        queryset=MOB.objects.values_list('nome', flat=True), 
        label='MOBO'
    )

    # Field for selecting the GAB
    # Queryset is a list of all GABs in the database
    # Label is the text displayed above the drop-down menu
    gab = forms.ModelChoiceField(
        queryset=GAB.objects.values_list('nome', flat=True), 
        label='GAB'
    )

class CPUImportForm(forms.Form):
   csv_file = forms.FileField(label='Import CPU')

class GPUImportForm(forms.Form):
   csv_file = forms.FileField(label='Import GPU')

class PSUImportForm(forms.Form):
   csv_file = forms.FileField(label="Import PSU")

class MOBImportForm(forms.Form):
   csv_file = forms.FileField(label="Import MOB")

class RAMImportForm(forms.Form):
   csv_file = forms.FileField(label="Import RAM")

class STOImportForm(forms.Form):
   csv_file = forms.FileField(label="Import Storage")

class GABImportForm(forms.Form):
   csv_file = forms.FileField(label="Import Case")