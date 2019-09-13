from django.shortcuts import render
from django.views.generic import (
	ListView,
	UpdateView,
	DeleteView,
	CreateView
)
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class UsuariosList(ListView):
	model = Usuario

	def get_queryset(self):
		programa_logado = self.request.user.usuario.programa
		return Usuario.objects.filter(programa=programa_logado)

class UsuariosEdit(UpdateView):
	model = Usuario
	fields = ['nome', 'clienteassociado']

class UsuariosDelete(DeleteView):
	model = Usuario
	success_url = reverse_lazy('list_usuarios')

class UsuariosNovo(CreateView):
	model = Usuario
	fields = ['nome', 'clienteassociado']

	def form_valid(self, form): #interessante inserir uma cláusula if para usuários com sobrenomes iguais.
		usuario = form.save(commit=False) # salva na memória mas não joga para o BD
		username = usuario.nome.split(' ')[0] + usuario.nome.split(' ')[1]
		usuario.programa = self.request.user.usuario.programa
		usuario.user = User.objects.create(username=username)
		usuario.save()
		return super(UsuariosNovo, self).form_valid(form)
