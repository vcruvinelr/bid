from django.db import models


class Programa(models.Model):
    nome = models.CharField(max_length=200, help_text='Nome do Programa')
