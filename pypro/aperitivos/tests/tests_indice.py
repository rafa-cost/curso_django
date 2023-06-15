import pytest
from django.test import TestCase
from django.urls import reverse
from pypro.diango_assertions import assert_contains
@pytest.fixture
def resp(client):
    return client.get(
        reverse('aperitivos:indice'))  # no meu intender , aperitivos chamando indice, ou seja na barra de endereço ao colocar aperitivos, chama
                                       # o indice.html
def test_status_code(resp):
    assert resp.status_code == 200  # codigo de sucesso ao acessar a pagina, da lista de código de status http
@pytest.mark.parametrize(
    'slug',
    [
        'Video Aperitivo: Motivação',
        'Instalação Windows'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)
@pytest.mark.parametrize(
    'slug',
    [
        'motivacao',
        'instalacao-windows'
    ]
)
def test_link_video(resp, slug): #esta logica esta transformando o nome dos videos em links que direcionam para o video selecionado
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')







