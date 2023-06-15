import pytest
from django.test import TestCase
from django.urls import reverse

from pypro.diango_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',))) #essa string 'motivacao' é o nome da pagina por isso para acessar, colocamos
                                                                        # ..../aperitivos/motivacao
def test_status_code(resp):
    assert resp.status_code == 200   #codigo de sucesso ao acessar a pagina, da lista de código de status http
# Create your tests here.

def test_titulo_video(resp): #esse teste é o do titulo do video
    assert_contains(resp, 'Video Aperitivo: Motivação')

def test_conteudo_video(resp):  #esse teste mostra o video na pagina
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/795707937"')






