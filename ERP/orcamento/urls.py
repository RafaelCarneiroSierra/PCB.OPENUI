from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('login', views.login, name='login'),
    path('partpicker', views.partpicker, name='partpicker'),
    path('import-csv/', views.import_cpu, name='import_cpu'),
    path('success/', views.success_page, name='success_page'),
    path('import-gpu/', views.import_gpu, name='import_gpu')
]

