from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import(
    ClientesList,
    ClientesNovo
)

urlpatterns = [
    path('list/', ClientesList.as_view(), name="list_clientes"),
    path('novo/', ClientesNovo.as_view(), name="create_cliente")
]
