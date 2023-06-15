from django.shortcuts import render
from django.urls import reverse
from pypro.diango_assertions import assert_contains
class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):                               #o get_absolute_url ira no indice.html ira converter os nomes do videos em links, que
        return reverse('aperitivos:video', args=(self.slug,))#que vai direcionar para o video selecionado


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 795707937),
    Video('instalacao-windows', 'Instalação Windows', 808002541),
]
videos_dct = {v.slug: v for v in videos}
def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos}) # retornar reinderizar , aperitivos/indice.html, passando como
def video(request, slug):                                                        #contexto a lista videos, para enumerar os videos.
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})#retornando reinderizando aperitivos/video.html, passando como contexto
                                                                             #video , que esta pegando video_dct, assim pegando o slug do video



