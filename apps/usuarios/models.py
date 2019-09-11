from django.db import models
from django.contrib.auth.models import User
from apps.programas.models import Programa
from apps.clientes.models import Cliente

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    clienteassociado = models.ManyToManyField(Cliente)
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome
