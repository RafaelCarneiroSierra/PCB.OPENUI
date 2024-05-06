from django.db import models

# Create your models here.
class CPU(models.Model):
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class GPU(models.Model):
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class RAM(models.Model): 
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class PSU(models.Model): 
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)

class MOB(models.Model): 
    nome = models.CharField(max_length=16)
    custo = models.CharField(max_length=16)
    preco = models.CharField(max_length=16)