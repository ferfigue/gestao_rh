from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    nome = models.CharField("Nome", max_length=50)
    
    def get_absolute_url(self):
        return reverse('index')
    
    def __str__(self) -> str:
        return self.nome
    
    