from django.db import models

# Create your models here.
class CPU:
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class GPU:
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class RAM: 
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class PSU: 
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class MOB: 
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)