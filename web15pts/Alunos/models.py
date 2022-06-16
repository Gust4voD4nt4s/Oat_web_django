from django.db import models

class Aluno(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nome_do_responsavel = models.CharField(max_length=100)
