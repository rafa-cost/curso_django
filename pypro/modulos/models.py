from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse

#esse modulo é como configuramos nossas tabelas no banco de dados, ou seja os campos que terão nas tabelas, depois de criar os campos fazemos o
#mng makemigrations , depois o mng miigrate, para passar as configurações para o banco.
# Create your models here.
class Modulo(OrderedModel): #OrderedModels serve para organizarmos os modulos da forma que quizermos
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()
    slug = models.SlugField(unique=True) #isso é um campo unico

    class Meta(OrderedModel.Meta): #OrderedModels serve para organizarmos os modulos da forma que quizermos
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})