import pytest
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.diango_assertions import assert_contains

@pytest.fixture
def videos(db):                          #consultando o banco
    return mommy.make(Video, 3) #esta pegando a classe Video de modulo models, esse 3 quer dizer 3 videos

@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))  # revertendo para app aperitivos chamando indice views

def test_status_code(resp):
    assert resp.status_code == 200  # codigo de sucesso ao acessar a pagina, da lista de código de status http

def test_titulo_video(resp, videos):
    for video in videos:             #separando todos os videos por unidade e vendo se todos estão nomeados
        assert_contains(resp, video.titulo)

def test_link_video(resp, videos): #
    for video in videos:             #separando os videos unitariamente
        video_link = reverse('aperitivos:video', args=(video.slug,))   #vendo se o link funciona, quando o usuario aperta no link e é direcionado para o video
        assert_contains(resp, f'href="{video_link}"')                           #'aperitivos:video', app aperitivos chamando video de views, args=(video.slug,) video escolhido pelo usuario
                                                                                #assert_contains(resp, f'href="{video_link}"'), confirmando se o link funciona






