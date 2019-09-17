from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    DiarioList,
    DiarioEdit,
    DiarioDelete,
    DiarioNovo
)

urlpatterns = [
    path('', DiarioList.as_view(), name="list_diarios"),
    path('editar/<int:pk>', DiarioEdit.as_view(), name="edit_diarios"),
    path('deletar/<int:pk>/', DiarioDelete.as_view(), name="delete_diario"),
    path('novo/', DiarioNovo.as_view(), name="create_diario")
]
