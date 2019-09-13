from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Cliente

class ClientesList(ListView):
    model = Cliente

    def get_queryset(self):
        programa_logado = self.request.user.usuario.programa
        return Cliente.objects.filter(programa=programa_logado)

class ClientesNovo(CreateView):
    model = Cliente
    fields = ['nome']

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.programa = self.request.user.usuario.programa
        cliente.save()
        return super(ClientesNovo, self).form_valid(form)
