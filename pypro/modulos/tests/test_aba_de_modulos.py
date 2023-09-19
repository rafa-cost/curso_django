import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):                        #usando o banco de dados
    return mommy.make(Modulo, 2) #esse 2 quer dizer que ele tera 2 modulos
@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home')) #aqui no meu entender é pra ver se o botão módulos esta aparecendo na view base:home (base/home.html)
    return resp


def test_titulo_dos_modulos(resp, modulos):  #aqui eu entendo que esta testando se os titulos da aba modulos estão aparecendo, ao clicar no botão. Na pagina home.html
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)


def test_link_dos_modulos(resp, modulos):   #aqui eu entendo que ao clicar em algum titulo de módulo, sera direcionado para a pagina do modulo
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())














