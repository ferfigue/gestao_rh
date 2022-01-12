from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Funcionario
from .forms import FuncionarioForm


class FuncionariosList(ListView):
    model = Funcionario
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)
 
class FuncionarioUpdate(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    
    def get_form_kwargs(self):
        kwargs = super(FuncionarioUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')
    
class FuncionarioNew(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
       
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username = username)
        funcionario.save()
        return super(FuncionarioNew, self).form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(FuncionarioNew, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    
        
    
    