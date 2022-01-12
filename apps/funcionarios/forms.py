from django.forms import ModelForm
from .models import Funcionario
from apps.departamentos.models import Departamento

class FuncionarioForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        self.fields['departamentos'].queryset = Departamento.objects.filter(
            empresa=user.funcionario.empresa
        )
    
    class Meta:
        model = Funcionario
        fields = ['nome', 'departamentos']