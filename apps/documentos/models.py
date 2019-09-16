from django.db import models
from apps.usuarios.models import Usuario
from django.shortcuts import reverse


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_usuarios', args=[self.proprietario.id])
        
    def __str__(self):
        return self.descricao
