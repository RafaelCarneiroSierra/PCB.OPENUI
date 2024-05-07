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
    
class PSU:
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    power = models.CharField(max_length=16, default='Memória')
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome

class MOB:
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    lga = models.CharField(max_length=16, default='Socket')
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome
    
class RAM: 
    tipo = models.CharField(max_length=16)
    nome = models.CharField(max_length=16)
    barramento = models.CharField(max_length=16, default='Tipo')
    custo = models.FloatField()
    preco = models.FloatField()
    
    def __str__(self):
        return  self.nome