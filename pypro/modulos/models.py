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

#criamos essa tabela modulos_aula depois de criarmos a tabela modulos_modulo, ou seja na sequência sem precisar dar
#o "migrate zero".
class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True) #isso é um campo unico
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT) #Foreignkey é uma chave estrangeira, e esse on_delete é sobre deletar o módulo e esse Protect é para proteger as aulas que estarão ligadas ao módulo que no caso sera deletado.
    order_with_respect_to = 'modulo'
    vimeo_id = models.CharField(max_length=32) #esse campo iremos colocar o número do video, que no caso vamos pegar do site vimeo

    class Meta(OrderedModel.Meta): #OrderedModels serve para organizarmos os modulos da forma que quizermos
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug})







