import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2) #esse 2 quer dizer que ele tera 2 modulos
@pytest.fixture
def resp(client, modulos): #modulos é o nome do aplicativo
    resp = client.get(reverse('base:home')) #aqui a função resp esta chamando o html base
    return resp


def test_titulo_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)

def test_link_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_asolute_url())














