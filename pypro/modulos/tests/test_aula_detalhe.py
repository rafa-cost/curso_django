import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):                 #usando o banco de dados
    return mommy.make(Modulo)   #aqui é o models class Modulo como parametro

@pytest.fixture
def aula(modulo):                      #no meu intender ele esta ligando a aula ao seu modulo
    return mommy.make(Aula, modulo=modulo)

@pytest.fixture
def resp(client_com_usuario_logado, aula):    # esses 3 testes abaixo para passar o usuario precisa estar logado, para ter acesso a esse conteudo do site, por isso passamos o client_com_usuario_logado que foi criado em coftest
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))   #o usuario só consegue acessar 'app modulos views aula' se estiver logado
    return resp

def test_titulo(resp, aula: Aula):        #testando o titulo da aula
    assert_contains(resp, aula.titulo)

def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"') #esta testando se o vimeo video esta funcionando na pagina

def test_modulo_breadcrumb(resp, modulo: Modulo):                              #esse teste indica se o breadcrumb esta funcionando na pagina do video, breadcrumb ele é referente as 3 barras que aparecem em cima do titulo (ex: home/modulo da aula/titulo da aula)
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')

@pytest.fixture
def resp_sem_usuario(client, aula):    # um cliente sem estar logado, tentando acessar as aulas
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))    #acessando app modulos views aula, kwargs={'slug': aula.slug} aqui é referente ao video que o usuario escolhe
    return resp

def test_usuario_nao_logado_redirect(resp_sem_usuario):   # esse teste é para ver se esta funcionando o redirecionamento do usuario não logado ao tentar acessar as aulas, ele sera redirecionado para fazer o login
    assert resp_sem_usuario.status_code == 302     #esse codigo 302 é o redirecionamento
    assert resp_sem_usuario.url.startswith(reverse('login'))   #nome da url





























