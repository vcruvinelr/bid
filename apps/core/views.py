from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from apps.programas.models import Programa


@login_required
def home(request):
	data = {}
	data['usuario'] = request.user
	return render(request, 'core/home.html', data)

@login_required
def cadastros(request):
	data = {}
	data['usuario'] = request.user
	return render(request, 'core/cadastros.html', data)

@login_required
def diarios(request):
	data = {}
	data['usuario'] = request.user
	return render(request, 'core/diarios.html', data)
