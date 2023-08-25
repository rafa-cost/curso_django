import pytest
from django.test import Client
from pypro.diango_assertions import assert_contains
from django.urls import reverse


# esses aqui  são os testes da pagina principal do projeto 'home.html'
@pytest.fixture
def resp(client, db):     #conectando o banco de dados
    resp = client.get(reverse('base:home'))   #o resp esta direcionando para direciona home.html
    return resp
def test_status_code(resp):
    assert resp.status_code == 200

def test_title(resp): #teste do titulo da pagina
    assert_contains(resp, '<title>Python Pro - Home</title>')  #"assert_contains" <- isso serve para confirmar o conteudo do teste

def test_home_link(resp): #testando o link que fica na parte de cima do lado esquerdo 'Python Pro'
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')

def test_email_link(resp):    #o email que fica no rodapé da pagina
    assert_contains(resp, 'href="mailton:ramalho@python.pro.br"')














