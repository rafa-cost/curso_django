from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video


def indice(request):
    videos = Video.objects.order_by('creation').all() # aqui é código que esta pegando os videos do banco de dados, esta fazendo ligação com a classe Videos de módulo models, pegando o campo creation.
    return render(request, 'aperitivos/indice.html', context={'videos': videos}) # retornar reinderizar , aperitivos/indice.html, passando como contexto a lista videos, para enumerar os videos.
def video(request, slug):
    video = get_object_or_404(Video, slug=slug) # se por acaso o video não for encontrado, vai dar a pagina de erro 404.
    return render(request, 'aperitivos/video.html', context={'video': video})#retornando reinderizando aperitivos/video.html, passando como contexto o video




