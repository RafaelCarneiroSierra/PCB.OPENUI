from django import forms
from .models import *

class cpuform(forms.Form):
   CPU = forms.ChoiceField(choices="", label="CPU")

   GPU = forms.ChoiceField(choices="", label="GPU")

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