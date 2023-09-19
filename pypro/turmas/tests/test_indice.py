import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):                           #acessando o banco
    return client.get(reverse('turmas:indice')) #app turmas acessando indice views

def test_status_code(resp):                    #teste de acesso bem sucedido
    assert resp.status_code == 200