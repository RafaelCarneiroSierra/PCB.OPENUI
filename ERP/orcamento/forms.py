from django import forms
from .models import *

class CpuSelectForm(forms.Form):
    cpu = forms.ModelChoiceField(queryset=CPU.objects.values_list('nome', flat=True), label='CPU')

class GpuSelectForm(forms.Form):
    gpu = forms.ModelChoiceField(queryset=GPU.objects.values_list('nome', flat=True), label='GPU')

class PSUSelectForm(forms.Form):
    psu = forms.ModelChoiceField(queryset=PSU.objects.values_list('nome', flat=True), label='PSU')

class MobSelectForm(forms.Form):
    mob = forms.ModelChoiceField(queryset=MOB.objects.values_list('nome', flat=True), label='MOB')

class RamSelectForm(forms.Form):
    ram = forms.ModelChoiceField(queryset=RAM.objects.values_list('nome', flat=True), label='RAM')

class GabSelectForm(forms.Form):
    gab = forms.ModelChoiceField(queryset=GAB.objects.values_list('nome', flat=True), label='GAB')

class stoSelectForm(forms.Form):
    sto = forms.ModelChoiceField(queryset=STO.objects.values_list('nome', flat=True), label='STO')

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