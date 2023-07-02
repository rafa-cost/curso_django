import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):    #essa fixture tem que ter acesso ao banco de dados
    return client.get(reverse('turmas:indice'))

def test_status_code(resp):
    assert resp.status_code == 200