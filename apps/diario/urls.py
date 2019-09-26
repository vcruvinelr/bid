from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    DiarioList,
    DiarioEdit,
    DiarioEditUsuario,
    DiarioDelete,
    DiarioNovo,
    VerificouDiario,
    DesmarcouDiario,
)

urlpatterns = [
    path('', DiarioList.as_view(), name="list_diarios"),
    path('editardiario/<int:pk>', DiarioEditUsuario.as_view(), name="edit_diarios_usuario"),
    path('editar/<int:pk>', DiarioEdit.as_view(), name="edit_diarios"),
    path('verificou-diario/<int:pk>/', VerificouDiario.as_view(), name="verificou_diario"),
    path('desmarcou-diario/<int:pk>/', DesmarcouDiario.as_view(), name="desmarcou_diario"),
    path('deletar/<int:pk>/', DiarioDelete.as_view(), name="delete_diario"),
    path('novo/', DiarioNovo.as_view(), name="create_diario")
]
