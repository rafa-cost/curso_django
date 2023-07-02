import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)

@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)

@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp

def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)

def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"') #com esse código iremos acrescentar os videos nas aulas

def test_modulo_breadcrumb(resp, modulo: Modulo): #esse código abaixo é responsavel pelo breadcrumb, ou seja praticamente ele indica o modulo e a aula que vc esta assistindo, no canto superior esquerdo
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')































