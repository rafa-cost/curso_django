import pytest
from model_mommy import mommy

from pypro.modulos import facade
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):                 #acessando o banco
    return [mommy.make(Modulo, titulo=s) for s in 'Antes Depois'.split()] # estamos criando 2 modulos com os titulos antes e depois

def test_listar_modulos_ordenados(modulos):     #aqui estamos testando se funciona a lista de modulos ser ordenada pelo order
    assert list(sorted(modulos, key=lambda modulo: modulo.order)) == facade.listar_modulos_ordenados()