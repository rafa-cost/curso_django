import pytest
from django.test import Client
from model_mommy import mommy

from pypro.diango_assertions import assert_contains
from django.urls import reverse

from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):             #acessando o banco
    return mommy.make(Modulo) #class Modulo como parametro

@pytest.fixture
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo) #estamos criando 3 aulas, a unica coisa que vamos mudar aqui, é que o atributo modulo da aula tem que estar conectado com o objeto modulo que é criado na fixture
                                                      #o atributo modulo que é criado em aula tem que estar conectado ao objeto modulo  que é criado na 1º fixture acima
@pytest.fixture
def resp(client, modulo, aulas): #modulo e aula foram criados nas 2 fixture acima
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))     #testando as variaveis em detalhe views, slug aqui é para pegar o modulo certo que o usuario escolheu
    return resp


def test_titulo(resp, modulo: Modulo):    #testando o titulo de modulos
    assert_contains(resp, modulo.titulo)

def test_descricao(resp, modulo: Modulo):    #testando a descrição de modulos
    assert_contains(resp, modulo.descricao)

def test_publico(resp, modulo: Modulo):     #testando a descrição do publico
    assert_contains(resp, modulo.publico)

def test_aulas_titulos(resp, aulas):
    for aula in aulas:                        #esse teste é para ver se esta mostrando todos os titulo de as aulas
        assert_contains(resp, aula.titulo)

def test_aulas_links(resp, aulas):            #esse teste é referente aos links de cada aula, que assim que vc clíca é direcionada para o video
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())






















