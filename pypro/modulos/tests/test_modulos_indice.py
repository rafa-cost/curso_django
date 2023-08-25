from typing import List

import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2) #estamos craindo 2 módulos aqui

@pytest.fixture
def aulas(modulos):
    aulas=[]
    for modulo in modulos:   # esse código ira mostrar na pagina todos os modulos presentes no banco
        aulas.extend(mommy.make(Aula, 3, modulo=modulo))  #estamos criando aqui 3 aulas para cada modulo
    return aulas

@pytest.fixture
def resp(client, modulos, aulas):  #aqui declaramos as 2 fixtures criadas acima
    resp = client.get(reverse('modulos:indice'))  #quando chamar "modulos" na pagina de endereço, ira buscar "indice.html"
    return resp

def test_indice_disponivel(resp):
    assert resp.status_code == 200  #código de sucesso http

def test_titulo(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)

def test_descricao(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)

def test_publico(resp, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(resp, modulo.publico)

def test_aulas_titulos(resp, aulas: List[Aula]):  #teste do titulo de aula
    for aula in aulas:
        assert_contains(resp, aula.titulo)

def test_aulas_urls(resp, aulas: List[Aula]):  #aqui é o teste dos links de aulas 
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())

































