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
def resp(client_com_usuario_logado, aula):    # esses 3 testes abaixo para passar o usuario precisa estar logado, para ter acesso a esse conteudo do site, por isso passamos o client_com_usuario_logado que foi criado em coftest
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp

def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)

def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"') #com esse código iremos acrescentar os videos nas aulas

def test_modulo_breadcrumb(resp, modulo: Modulo): #esse código abaixo é responsavel pelo breadcrumb, ou seja praticamente ele indica o modulo e a aula que vc esta assistindo, no canto superior esquerdo
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')

@pytest.fixture
def resp_sem_usuario(client, aula):    # essa fixture de resp_sem_usuario esta sendo passada como parametro, para a função abaixo test_usuario_nao_logado_redirect
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp

def test_usuario_nao_logado_redirect(resp_sem_usuario):   # esse teste é quando o usuario não esta logado e tenta ver os videos, ai ele é direcionado para o login
    assert resp_sem_usuario.status_code == 302     #esse codigo 302 é o redirecionamento temporario do http
    assert resp_sem_usuario.url.startswith(reverse('login'))





























