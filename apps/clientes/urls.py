from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import(
    ClientesList,
    ClientesNovo,
    ClienteEditar,
    ClienteDelete
)

urlpatterns = [
    path('list/', ClientesList.as_view(), name="list_clientes"),
    path('novo/', ClientesNovo.as_view(), name="create_cliente"),
    path('editar/<int:pk>/', ClienteEditar.as_view(), name="editar_cliente"),
    path('deletar/<int:pk>/', ClienteDelete.as_view(), name="delete_cliente"),
]
