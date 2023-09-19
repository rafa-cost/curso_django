from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=64)    #nome da turma
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()               #data do inicio do curso
    fim = models.DateField()                  #data do termino do curso
    alunos = models.ManyToManyField(get_user_model(), through='Matricula')     #pegando aqui a classe Metricula
                                                                               # "get_user_model" os usuarios serão os que vamos criar no app base. Os usuarios serão os alunos


class Matricula(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  #"get_user_model" os usuarios serão os que vamos criar no app base
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)               # e aqui pegando a classe turma

    class Meta:
        unique_together = [['usuario', 'turma']]    #esse unique_together ele coloca uma condição de unicidade, ou aqui no caso [['usuario', 'turma']], estamos querendo dizer que o mesmo usuario não pode se cadastrar mais de uma vez na mesma turma
        ordering = ['turma', 'data']               #estamos organizando a ordem de matriculas, ordenar primeiramente pela turma e as matriculas que estiverem na mesma turma , vamos ordenar pela data
                                                   #esse class Meta é uma configurção de modelo, a documentação dele esta no docs.djangoproject.com













