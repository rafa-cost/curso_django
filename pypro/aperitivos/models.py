from django.db import models
from django.urls import reverse


class Video(models.Model):

    titulo = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    vimeo_id = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):  # o get_absolute_url ira no indice.html ira converter os nomes do videos em links, que
        return reverse('aperitivos:video', args=(self.slug,))  # vai direcionar para o video selecionado

    def __str__(self):
        return f'Video: {self.titulo}' #esse codigo ele imprimi o titulo do video, na parte de cima da tela, assim que adicionamos um novo video, ou quando alteramos algo no video
