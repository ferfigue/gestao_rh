from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Departamento


class DepartamentoList(ListView):
    model = Departamento
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)
 
class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome',]
    
class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
    
class DepartamentoNew(CreateView):
    model = Departamento
    fields = ['nome',]
    
    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoNew, self).form_valid(form)
        
    