import pytest
from model_mommy import mommy


#esse modulo pelo que eu entendi, ele é responsavel pela parte do nosso site que o usuario acessa só depois de logado
#ele é responsavel pelos testes , vamos emular um usuario cadastrado e logado
@pytest.fixture
def usuario_logado(db, django_user_model): #aqui no meu entender esta emulando um usuario cadastrado no banco, com seus dados
    usuario_modelo = mommy.make(django_user_model, first_name='Fulano') #first_name='Fulano'a gente coloca isso , pq vamos usar esse "def usuario_logado" para fazer o "test_nome_usuario_logado_disponivel", pra isso precisamos que o usuario tenha um nome
    return usuario_modelo
@pytest.fixture
def client_com_usuario_logado(usuario_logado, client):  #e aqui esta emolundo um usuario logado
    client.force_login(usuario_logado)
    return client