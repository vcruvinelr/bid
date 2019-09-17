from django.db import models

class Cobrape(models.Model):
    escritorio = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)

    def __str__(self):
        return self.escritorio

class Consorcio(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
