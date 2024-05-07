from django import forms
from .models import *

class cpuform(forms.Form):
   CPU = forms.ChoiceField(choices="", label="CPU")

   GPU = forms.ChoiceField(choices="", label="GPU")

class CSVImportForm(forms.Form):
   csv_file = forms.FileField()