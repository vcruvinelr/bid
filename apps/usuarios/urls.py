from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    UsuariosList,
    UsuariosEdit,
    UsuariosDelete,
    UsuariosNovo,
    Pdf
)

from .views import pdf_reportlab

urlpatterns = [
    path('', UsuariosList.as_view(), name="list_usuarios"),
    path('editar/<int:pk>/', UsuariosEdit.as_view(), name="update_usuarios"),
    path('deletar/<int:pk>/', UsuariosDelete.as_view(), name="delete_usuarios"),
    path('novo/', UsuariosNovo.as_view(), name="create_usuarios"),
    path('pdf-reportlab/', pdf_reportlab, name='pdf_reportlab'),
    path('relatorios/', Pdf.as_view(), name='relatoriosusuarios'),
]
