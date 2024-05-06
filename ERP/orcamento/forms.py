from django import forms
from .models import *

class cpuform(forms.Form):
   CPU = forms.ChoiceField(choices="")