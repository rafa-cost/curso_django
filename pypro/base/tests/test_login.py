import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.diango_assertions import assert_contains, assert_not_contains

#aqui são os testes da pagina de login.html
@pytest.fixture
def resp(client, db):    # db conexão com o banco de dados
    return client.get(reverse('login'))   #nome da url

def test_login_form_page(resp):     #teste de acesso a pagina
    assert resp.status_code == 200

@pytest.fixture
def usuario(db, django_user_model):    # django_user_model me traz a classe de criação do usuario
    usuario_modelo = mommy.make(django_user_model)    #vamos usar o mommy.make , para construir esse campo de cadastro 'usuario_modelo'.
    senha = 'senha'     #essa parte abaixo faz parte da criação de senha
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plena = senha
    return usuario_modelo               #Aqui estamos emulando um usuario salvo no banco de dados com a senha que ele queria
@pytest.fixture
def resp_post(client, usuario):    #vamos receber esses dados do dicionario antes de fazer a chamada post. Ou seja esta vendo se as variaveis daqui e do html estão se conectando pelo contexto.
    return client.post(reverse('login'), {'username': usuario.email,'password': usuario.senha_plena})

def test_login_redirect(resp_post):     #esse é o teste de login que vai direcionar para o modulo indice(onde estão os modulos e aulas do curso)
    assert resp_post.status_code == 302   #codigo de redirecionamento 302
    assert resp_post.url == reverse('modulos:indice')   #ou seja redirecionando o usuario para o app modulos de views indice (praticamente modulos/indice.html)
                                                        #esse código tem uma complementação no settings (LOGIN_REDIRECT_URL = '/modulos/')
@pytest.fixture
def resp_home(client, db):                     #se conectando com o banco de dados
    return client.get(reverse('base:home'))    # ve se esta direcionando para app base views home, que é a pagina de entrada do site
def test_botao_entrar_disponivel(resp_home):     #teste botão entrar, estara disponivel assim que o usuário acessar o site
    assert_contains(resp_home, 'Entrar')

def test_link_de_login_disponivel(resp_home):    #o teste pra ver se o botão de login esta disponivel
    assert_contains(resp_home, reverse('login'))
@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):    #usuario logado , acessando o banco
    return client_com_usuario_logado.get(reverse('base:home'))      #retornar usuario logado , pegar , reverter para aplicate base views home. ou seja quando o usario estiver logafo em home.html

def test_botao_entrar_indisponivel(resp_home_com_usuario_logado):  # depois que o usuario se loga o botão 'entrar' tem que desaparecer, é o teste para ver se o botão esta indisponivel
    assert_not_contains(resp_home_com_usuario_logado, 'Entrar')

def test_link_de_login_indisponivel(resp_home_com_usuario_logado):   #é o teste de quando o usuario estiver logado o botão de login, tem que estar indisponivel
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))

def test_botao_sair_disponivel(resp_home_com_usuario_logado):    #botão sair tem que estar disponivel assim que o usuario se logar, esse é o teste
    assert_contains(resp_home_com_usuario_logado, 'Sair')

def test_nome_usuario_logado_disponivel(resp_home_com_usuario_logado, usuario_logado):    # quando o usuario se logar o nome dele aparecera no lugar do botão entrar
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)               #dos testes aqui é o unico que pega o "usuario_logado.first_name" pq aqui eu preciso dos dados do usuario logado, no caso o nome

def test_link_de_logout_disponivel(resp_home_com_usuario_logado):    #esse teste acho que é para ver se o botão sair esta funcionando , direcionando para a pagina home após a saida
    assert_contains(resp_home_com_usuario_logado, reverse('logout'))









