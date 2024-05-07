from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('login', views.login, name='login'),
    path('partpicker', views.partpicker, name='partpicker'),
    path('import-csv/', views.import_csv, name='import_csv'),
    path('success/', views.success_page, name='success_page')
]

