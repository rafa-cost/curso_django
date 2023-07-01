from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()    #data do inicio do curso
    fim = models.DateField()       #data do termino do curso
    alunos = models.ManyToManyField(get_user_model(), through='Matricula')


class Matricula(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) #chave estrangeira acho que tem em comum, que ela da para armazenar e apagar as informações se quiser
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['usuario', 'turma']]
        ordering=['turma', 'data']