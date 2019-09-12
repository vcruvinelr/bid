from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario


@login_required
def home(request):
	data = {}
	data['usuario'] = request.user 
	return render(request, 'core/home.html', data)