from django.db import models

class Turmas(models.Model):

    Aluno = models.CharField(max_length=100)
    Quantidade_de_faltas = models.CharField(max_length=100)
    Notificações = models.CharField(max_length=100)
