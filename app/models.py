# Create your models here.

from django.db import models
from django.contrib.auth.models import User   

class Item(models.Model):  
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):  
        return self.nome  
    
class Acessorio(models.Model):  
    nome = models.CharField(max_length=100) 
    item = models.ForeignKey(Item, on_delete=models.CASCADE) 

    def __str__(self):   
        return self.nome  
    
