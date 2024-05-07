from django.db import models

# Create your models here.
class CPU(models.Model):
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    score = models.IntegerField()
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome
class GPU(models.Model):
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    score = models.IntegerField()
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome
    
class PSU(models.Model):
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome

class MOB(models.Model):
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome
    
class RAM(models.Model): 
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome
    
class STO(models.Model): 
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome
    
class GAB(models.Model): 
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=32)
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome