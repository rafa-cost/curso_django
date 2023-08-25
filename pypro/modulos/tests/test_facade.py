import pytest
from model_mommy import mommy

from pypro.modulos import facade
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in 'Antes Depois'.split()] # estamos criando 2 modulos com os titulos antes e depois

def test_listar_modulos_ordenados(modulos):     #no meu entendimento aqui seria um teste, para genter colocar os modulos que aparecem na hora que clicamos no botão modulos, organizar na ordem que a gente quiser. Isso tudo esta configurado em módulo facade, aqui é somente o teste
    assert list(sorted(modulos, key=lambda modulo: modulo.order)) == facade.listar_modulos_ordenados()