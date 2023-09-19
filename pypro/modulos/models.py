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
    slug = models.SlugField(unique=True) #isso é um campo unico, slug sempre sera campo unico

    class Meta(OrderedModel.Meta): #OrderedModels serve para organizarmos os modulos da forma que quizermos
        pass

    def __str__(self):
        return self.titulo  #esse codigo ele imprimi o titulo do video, na parte de cima da tela, assim que adicionamos um novo video, ou quando alteramos algo no video, isso dentro do admin do django

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug}) # o get_absolute_url ira converter os nomes dos modulos em links e vai direcionar para a pagina do modulo (modulo_detalhe). A questão do "kwargs={'slug': self.slug}" é para diferenciar um modulo do outro.
                                                                               #esse "modulos" é o nome da pasta que guarda o templates. Aqui o modulos esta fazendo referencia a views detalhe
class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)                               #isso é um campo unico
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT) #Aqui estamos fazendo a conexão entre modulos e aulas no banco de dados, essa conexão é o seguinte é de 1 para muitos ou seja um modulo pode ter varias aulas, agora as aulas podem ter apenas 1 modulo.
                                                                      #Foreignkey é uma chave estrangeira. Onde estamos iformando o nome do modelo que vamos relacionar 'Modulo'(que aparentemente é o nome da classe). E esse on_delete é sobre deletar o módulo , o que acontecera com as aulas caso eu delete o modulo. Utilizamos Protect ou seja o modulo só podera ser apagado caso não tenha aulas ligadas a ele. Agora se eu utilizasse o CASACADE as aulas seriam apagadas junto com o modulo
    order_with_respect_to = 'modulo'     #aqui é o seguinte com relação a quem o "order" sera considerado e no caso aqui é o campo "modulo"
    vimeo_id = models.CharField(max_length=32) #esse campo iremos colocar o número do video, que no caso vamos pegar do site vimeo

    class Meta(OrderedModel.Meta): #OrderedModels serve para organizarmos os modulos da forma que quizermos
        pass

    def __str__(self):
        return self.titulo #esse codigo ele imprimi o titulo do video, na parte de cima da tela, assim que adicionamos um novo video, ou quando alteramos algo no video, isso dentro do admin do django


    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug}) # o get_absolute_url ira converter os nomes dos videos em links e vai direcionar para o video selecionado
                                                                            ##esse "modulos" é o nome da pasta que guarda o templates. aqui o modulos esta fazendo referencia a view aula. Onde também sera referenciado através do seu slug







