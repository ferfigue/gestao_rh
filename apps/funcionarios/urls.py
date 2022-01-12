
from django.urls import path
from .views import  FuncionariosList, FuncionarioUpdate, FuncionarioDelete, FuncionarioNew

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionario'),
    path('novo/', FuncionarioNew.as_view(), name='new_funcionario'),
    path('editar/<int:pk>', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
