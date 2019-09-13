from django.db import models
from apps.programas.models import Programa
from django.urls import reverse

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_clientes')
