from django.shortcuts import render
from django.urls import reverse

from pypro.aperitivos.models import Video



videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id=795707937),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id=808002541),
]
videos_dct = {v.slug: v for v in videos}
def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos}) # retornar reinderizar , aperitivos/indice.html, passando como
def video(request, slug):                                                        #contexto a lista videos, para enumerar os videos.
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})#retornando reinderizando aperitivos/video.html, passando como contexto
                                                                             #video , que esta pegando video_dct, assim pegando o slug do video



