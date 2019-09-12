from django.shortcuts import render
from django.views.generic import ListView
from .models import Usuario

class UsuariosList(ListView):
	model = Usuario
