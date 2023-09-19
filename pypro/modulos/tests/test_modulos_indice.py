from typing import List

import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):                  #acessando o banco
    return mommy.make(Modulo, 2) #class Modulo passada como parametro

@pytest.fixture
def aulas(modulos):
    aulas=[]                 #aqui esta indicando que serão varias aulas por módulo
    for modulo in modulos:   # esse teste é para ver se aparece na pagina todos os modulos que existem no banco de dados
        aulas.extend(mommy.make(Aula, 3, modulo=modulo))  #estamos criando aqui 3 aulas para cada modulo
    return aulas                 #retornando todas as aulas criadas em módulos na fixture acima def "modulos(db): "

@pytest.fixture
def resp(client, modulos, aulas):  #aqui passamos como parametro as 2 fixtures criadas acima
    resp = client.get(reverse('modulos:indice'))  #estamos testando essas 2 (modulos, aulas) variaveis dentro de indice views, aqui não passamos o slug como parametro pois estamos pegando todos os modulos então não precisa identificar
    return resp

def test_indice_disponivel(resp):
    assert resp.status_code == 200  #código de sucesso http

def test_titulo(resp, modulos: List[Modulo]):        #teste dos titulos de modulos
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)

def test_descricao(resp, modulos: List[Modulo]):     #teste das descrições de modulos
    for modulo in modulos:
        assert_contains(resp, modulo.descricao)

def test_publico(resp, modulos: List[Modulo]):      #teste de publico de modulos
    for modulo in modulos:
        assert_contains(resp, modulo.publico)

def test_aulas_titulos(resp, aulas: List[Aula]):  #teste do titulo de aula
    for aula in aulas:
        assert_contains(resp, aula.titulo)

def test_aulas_urls(resp, aulas: List[Aula]):  #aqui é o teste dos links de aulas 
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())

































