from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import UsuariosList, UsuariosEdit

urlpatterns = [
    path('', UsuariosList.as_view(), name="list_usuarios"),
    path('editar/<int:pk>/', UsuariosEdit.as_view(), name="update_usuarios")
]
