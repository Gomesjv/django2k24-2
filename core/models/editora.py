from django.db import models 

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_legth=200, blank=True, null=True)