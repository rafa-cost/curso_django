import pytest
from django.test import Client
from pypro.diango_assertions import assert_contains
from django.urls import reverse

@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp
def test_status_code(resp):
    assert resp.status_code == 200

def test_title(resp): #titulo da pagina
    assert_contains(resp, '<title>Python Pro</title>')

def test_home_link(resp): #link que fica na parte de cima do lado esquerdo
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')







