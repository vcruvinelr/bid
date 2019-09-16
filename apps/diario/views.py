from django.shortcuts import render
from .models import Diario
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView


class DiarioList(ListView):
    model = Diario

    def get_queryset(self):
        programa_logado = self.request.user.usuario.programa
        return Diario.objects.filter(proprietario__programa=programa_logado)
