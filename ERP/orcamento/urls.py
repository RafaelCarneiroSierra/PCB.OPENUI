from django.urls import path
from . import views, importviews

urlpatterns = [
    path('', views.home, name='base'),
    path('login', views.login, name='login'),
    path('partpicker', views.partpicker, name='partpicker'),
    path('import-csv/', importviews.import_cpu, name='import_cpu'),
    path('success/', importviews.success_page, name='success_page'),
    path('import-gpu/', importviews.import_gpu, name='import_gpu'),
    path('import-psu/', importviews.import_psu, name='import_psu'),
    path('import-mob/', importviews.import_mob, name='import_mob'),
    path('import-ram/', importviews.import_ram, name='import_ram'),
    path('import-sto/', importviews.import_sto, name='import_sto'),
    path('import-gab/', importviews.import_gab, name='import_gab')
]

