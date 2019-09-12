from django.urls import path
from .views import ProgramaCreate, ProgramaEdit

urlpatterns = [
	path('novo/', ProgramaCreate.as_view(), name='create_programa'),
	path('editar/<int:pk>', ProgramaEdit.as_view(), name='edit_programa') #verificar documentação do django.urls, lá explica como posso utilizar as ids nas urls
]
