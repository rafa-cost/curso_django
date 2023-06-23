import pytest
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.diango_assertions import assert_contains

@pytest.fixture
def videos(db):
    return mommy.make(Video, 3) #esta pegando a classe Video de modulo models, esse 3 quer dizer 3 videos

@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))  # no meu intender , aperitivos chamando indice, ou seja na barra de endereço ao colocar aperitivos, chama
                                       # o indice.html
def test_status_code(resp):
    assert resp.status_code == 200  # codigo de sucesso ao acessar a pagina, da lista de código de status http

def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)

def test_link_video(resp, videos): #esta logica esta transformando o nome dos videos em links que direcionam para o video selecionado
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')







