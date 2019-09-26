import json
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
from django.urls import reverse_lazy, reverse
from django.views import View
from django.http import HttpResponse


class DiarioList(ListView):
    model = Diario

    def get_queryset(self):
        programa_logado = self.request.user.usuario.programa
        return Diario.objects.filter(proprietario__programa=programa_logado)

class DiarioEdit(UpdateView):
    model = Diario
    form_class = DiarioForm

    def get_success_url(self):
        return reverse_lazy('update_usuarios', args=[self.request.user.id])
        #return reverse('update_usuarios') #neste caso o object id será o nome do usuário! não confundir com o object.id do diario.

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

class DiarioEditUsuario(UpdateView):
    model = Diario
    form_class = DiarioForm
    #success_url = reverse_lazy('list_diarios')

    def get_success_url(self):
        #return reverse_lazy('edit_diarios_usuario', args=[self.request.user.id])
        return reverse_lazy('edit_diarios_usuario', args=[self.object.id])

    def get_form_kwargs(self): #metodo para injetar usuario no form
        kwargs = super(DiarioEditUsuario, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class VerificouDiario(View):
    def post(self, *args, **kwargs):
        registro_diario = Diario.objects.get(id=kwargs['pk'])
        registro_diario.lida = True #vem do models
        registro_diario.save()

        usuario = self.request.user.usuario
        response = json.dumps(
            {'diarios': 'Diários Restates a serem verificados pelo gestor: ' + str(usuario.total_registros_diario),
            'mensagem': usuario.nome+',' + ' A verificação do diário foi realizada com sucesso!'}
        )
        return HttpResponse(response, content_type='application/json')

class DesmarcouDiario(View):
    def post(self, *args, **kwargs):
        registro_diario = Diario.objects.get(id=kwargs['pk'])
        registro_diario.lida = False #vem do models
        registro_diario.save()

        usuario = self.request.user.usuario
        response = json.dumps(
            {'diarios01': 'Diários Restates a serem verificados pelo gestor: ' + str(usuario.total_registros_diario),
            'mensagem01': usuario.nome+',' + ' A desmarcação do diário foi realizada com sucesso!'}
        )
        return HttpResponse(response, content_type='application/json')
