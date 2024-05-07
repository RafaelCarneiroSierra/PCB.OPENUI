from django.db import models

# Create your models here.
class PCPART(models.Model):
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)