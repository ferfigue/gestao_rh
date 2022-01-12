from django.urls import path
from .views import DepartamentoEdit, DepartamentoList, DepartamentoEdit, DepartamentoDelete, DepartamentoNew

urlpatterns = [
    path('listar/', DepartamentoList.as_view(), name="list_departamentos"),
    path('editar/<int:pk>', DepartamentoEdit.as_view(), name="edit_departamentos"),
    path('deletar/<int:pk>', DepartamentoDelete.as_view(), name="delete_departamentos"),
    path('novo/', DepartamentoNew.as_view(), name="create_departamentos"),
]
