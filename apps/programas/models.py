from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Programa(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do Programa')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')
