from django.db import models
from apps.usuarios.models import Usuario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
