from django.shortcuts import render
from .models import Diario
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
from .forms import DiarioForm

class DiarioList(ListView):
    model = Diario

    def get_queryset(self):
        programa_logado = self.request.user.usuario.programa
        return Diario.objects.filter(proprietario__programa=programa_logado)

class DiarioEdit(UpdateView):
    model = Diario
    form_class = DiarioForm

    def get_form_kwargs(self): #metodo para injetar usuario no form
        kwargs = super(DiarioEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class DiarioDelete(DeleteView):
    model = Diario
    success_url = reverse_lazy('list_diarios')


class DiarioNovo(CreateView):
    model = Diario
    form_class = DiarioForm

    def get_form_kwargs(self): #metodo para injetar usuario no form
        kwargs = super(DiarioNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
