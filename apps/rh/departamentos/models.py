from django.db import models
from django.urls import reverse
from apps.rh.empresas.models import Empresa

class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    
    def get_absolute_url(self):
        return reverse('list_departamentos')
      
    def __str__(self):
        return self.nome