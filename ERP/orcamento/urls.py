from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('login', views.login, name='login'),
    path('partpicker', views.partpicker, name='partpicker')
]

