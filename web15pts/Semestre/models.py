from django.db import models

class Semestre(models.Model):

    va1 = models.CharField(max_length=100)
    va2 = models.CharField(max_length=100)
    va3 = models.CharField(max_length=100)
    oat = models.CharField(max_length=100)
