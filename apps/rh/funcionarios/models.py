from django.db import models
from django.urls import reverse
from django.db.models import Sum

from django.contrib.auth.models import User
from apps.rh.departamentos.models import Departamento
from apps.rh.empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField("Nome", max_length=50)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse('list_funcionario')
    
    @property #pode  ser chamado direto do templates
    def total_horas_extra(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        print(f'Debug app H.E: {total}')
        return total
    
    def __str__(self):
        return self.nome
    
    