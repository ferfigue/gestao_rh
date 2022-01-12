from django.db import models
from django.urls import reverse
from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    motivo = models.CharField(max_length=250)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField('Horas trabalhadas', max_digits=5, decimal_places=2)
    date_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def get_absolute_url(self):
        return reverse('list_hora_extras')
    
    def __str__(self):
        return self.motivo