from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField("Nome", max_length=50)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse('list_funcionario')
    
    def __str__(self):
        return self.nome
    
    