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
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo) #estamos criando 3 aulas, a unica coisa que vamos mudar aqui, é que o atributo modulo da aula tem que estar conectado com o objeto modulo que é criado na fixture

@pytest.fixture
def resp(client, modulo, aulas): #modulo é o nome do aplicativo
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp

#ao clicar no botão "modulos" da pagina de entrada ira aparecer as opções, e ao clicar nas opções essa pagina ira
#entrar em ação , mostrando o titulo do curso, descrição e publico. Que no caso é a pagina modulo_detalhe.html
def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)

def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)

def test_publico(resp, modulo: Modulo):     #descrição do publico
    assert_contains(resp, modulo.publico)

def test_aulas_titulos(resp, aulas):
    for aula in aulas:                        #esse teste é para mostrar todos os titulo de as aulas
        assert_contains(resp, aula.titulo)

def test_aulas_links(resp, aulas):            #esse teste é referente aos links de cada aula, que assim que vc clíca é direcionada para o video
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())






















