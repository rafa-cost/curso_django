import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.diango_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):    # db conexão com o banco de dados
    return client.get(reverse('login'))   #nome do html

def test_login_form_page(resp):
    assert resp.status_code == 200
                    #esse codigo ira criar o usuario no banco , com a senha de sua escolha
@pytest.fixture     # para executar o login , eu preciso que o usuario esteja salvo no meu banco, e a classe djando_user_model faz isso
def usuario(db, django_user_model):    # django_user_model me traz a classe de criação do usuario
    usuario_modelo = mommy.make(django_user_model)    #vamos usar o mommy.make , para construir esse campo de cadastro 'usuario_modelo'
    senha = 'senha'     #essa parte abaixo faz parte da criação de senha
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plena = senha
    return usuario_modelo
@pytest.fixture                   #esse resp esta executando uma chamada post, para o login
def resp_post(client, usuario):    #vamos receber esse dados do dicionario antes de fazer a chamada post
    return client.post(reverse('login'), {'username': usuario.email,'password': usuario.senha_plena})

def test_login_redirect(resp_post):     #esse é o teste de login, redirecionando a pagina depois do sucesso do login, para 'modulos:indice'
    assert resp_post.status_code == 302   #codigo de redirecionamento 302
    assert resp_post.url == reverse('modulos:indice')

@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))    #esse botão entrar, assim que o usuario colocar seus dados será direcionado para a pagina home, a pagina principal

def test_botao_entrar_disponivel(resp_home):     #o  botão de entrar estara disponivel assim que o usuário acessar o site, depois que ele se logar o botão desaparece
    assert_contains(resp_home, 'Entrar')

def test_link_de_login_disponivel(resp_home):    #o link de login onde coloca as informações para se logar
    assert_contains(resp_home, reverse('login'))
@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):    #esse botão entrar, assim que o usuario colocar seus dados será direcionado para a pagina home, a pagina principal
    return client_com_usuario_logado.get(reverse('base:home'))

def test_botao_entrar_indisponivel(resp_home_com_usuario_logado):  # depois que o usuario se loga o botão 'entrar' tem que desaparecer
    assert_not_contains(resp_home_com_usuario_logado, 'Entrar')    #o assert_not_contains ele faz o contrario do assert_contains, ele vai se certificar que o botão entrar não estara disponivel, assim que o usuario se logar

def test_link_de_login_indisponivel(resp_home_com_usuario_logado):   #assim que o usuario se logar pelo link de login, o link não aparecera mais
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))

def test_botao_sair_disponivel(resp_home_com_usuario_logado):    #botão sair tem que estar disponivel assim que o usuario se logar, na setinha ao lado do primeiro nome do usuario
    assert_contains(resp_home_com_usuario_logado, 'Sair')

def test_nome_usuario_logado_disponivel(resp_home_com_usuario_logado, usuario_logado):    # quando o usuario se logar o nome dele aparecera no lugar do botão entrar
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)

def test_link_de_logout_disponivel(resp_home_com_usuario_logado):    # esse teste é com relação ao botão sair estar disponivel
    assert_contains(resp_home_com_usuario_logado, reverse('logout'))  # no meu intender esta é a url nomeada









