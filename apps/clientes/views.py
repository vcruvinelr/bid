from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.urls import reverse_lazy

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

class ClienteEditar(UpdateView):
    model = Cliente
    fields = ['nome']

class ClienteDelete(DeleteView):
	model = Cliente
	success_url = reverse_lazy('list_clientes')
