from django.shortcuts import render
from .models import Documento
from django.views.generic import CreateView

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs): #override no post
        form = self.get_form()
        form.instance.proprietario_id = self.kwargs['usuario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
