import pytest
from django.test import Client
from pypro.diango_assertions import assert_contains
from django.urls import reverse


# esses aqui  são os testes da pagina principal do projeto 'home.html'
#o plugin do pytest django fornece um fixture que se chama client, este objeto é fornecido pelo proprio framework do django, ele serve pra gente emolar requisições http
@pytest.fixture
def resp(client, db):     #acessando o banco de dados
    resp = client.get(reverse('base:home'))   #app base levando para veiws home
    return resp
def test_status_code(resp):                  #vendo se a pagina esta conseguindo ser acessada com sucesso
    assert resp.status_code == 200

def test_title(resp):                         #teste do titulo da aba pagina
    assert_contains(resp, '<title>Python Pro - Home</title>')  #"assert_contains" <- isso serve para confirmar o conteudo do teste

def test_home_link(resp):                   # teste do link que fica na parte de cima do lado esquerdo 'Python Pro'. Que vai direcionar para views home
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')

def test_email_link(resp):                   #teste para ver se o email que fica no rodapé da  esta aparecendo
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')














