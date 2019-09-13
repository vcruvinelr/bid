from django.urls import path
from .views import home
from .views import cadastros

urlpatterns = [
    path('', home, name='home'),
    path('cadastros', cadastros, name='cadastros')
]
