from django.urls import path
from .views import home
from .views import cadastros
from .views import diarios

urlpatterns = [
    path('', home, name='home'),
    path('cadastros', cadastros, name='cadastros'),
    path('diarios', diarios, name='diarios')
]
