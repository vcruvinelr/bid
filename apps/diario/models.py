from django.db import models
from apps.programas.models import Programa
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario
from django.urls import reverse

class Diario(models.Model):
    titulo = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    descritivo = models.TextField(max_length=1000)
    data = models.DateField(auto_now=False)
    programa = models.ForeignKey(
    	Programa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('edit_diarios', args=[self.id])
