from django.db import models
from django.contrib.auth.models import User
from apps.programas.models import Programa
from apps.clientes.models import Cliente
from django.urls import reverse
from django.db.models import Sum, Count

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    clienteassociado = models.ManyToManyField(Cliente)
    programa = models.ForeignKey(
    	Programa, on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.nome

    @property
    def total_registros_diario(self):
        total = self.diario_set.all().aggregate(
            Count('titulo'))['titulo__count']
        return total


    def get_absolute_url(self):
        return reverse('list_usuarios')
