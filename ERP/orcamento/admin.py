from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(PSU)
admin.site.register(MOB)