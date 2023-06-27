import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)
@pytest.fixture
def resp(client, modulo): #modulo é o nome do aplicativo
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp

def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)

def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)

def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)














