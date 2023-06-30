from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()    #data do inicio do curso
    fim = models.DateField()       #data do termino do curso