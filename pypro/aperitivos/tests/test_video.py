import pytest
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.diango_assertions import assert_contains
from django.shortcuts import render, get_object_or_404


@pytest.fixture
def video(db):  #"db" banco de dados
    return mommy.make(Video) #o model mommy esta se baseando na classe "Video"

@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))

@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug + 'video_nao_existente',)))

def test_status_code_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404 # "404" código de pagina não encontrada, código de erro

def test_status_code(resp):
    assert resp.status_code == 200   #codigo de sucesso ao acessar a pagina, da lista de código de status http
# Create your tests here.

def test_titulo_video(resp, video): #esse teste é o do titulo do video
    assert_contains(resp, video.titulo)

def test_conteudo_video(resp, video):  #esse teste mostra o video na pagina
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')






