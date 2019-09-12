from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Programa

class ProgramaCreate(CreateView):
	model = Programa
	fields = ['nome']

	def form_valid(self, form):
		obj = form.save()
		usuario = self.request.user.usuario
		usuario.programa = obj
		usuario.save()
		return HttpResponse("Ok")

class ProgramaEdit(UpdateView):
	model = Programa
	fields = ['nome']
