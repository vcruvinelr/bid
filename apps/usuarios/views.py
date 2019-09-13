from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Usuario

class UsuariosList(ListView):
	model = Usuario

	def get_queryset(self):
		programa_logado = self.request.user.usuario.programa
		return Usuario.objects.filter(programa=programa_logado)

class UsuariosEdit(UpdateView):
	model = Usuario
	fields = ['nome', 'clienteassociado']
