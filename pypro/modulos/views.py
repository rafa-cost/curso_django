from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}             #variavel modulos do html pegando a função listar_modulos_com_aulas
    return render(request, 'modulos/indice.html', ctx)  #o contexto ira ser usado em 'modulos/indice.html'
# Create your views here.
def detalhe(request, slug):                   #a gente vai chegar no detalhe do modulo apartir do slug que é passado como parametro
    modulo = facade.encontrar_modulo(slug)    #dentro da variavel modulo, colocando a função facade.encontrar_modulo e passando slug como parametro
    aulas = facade.listar_aulas_de_modulos_ordenadas(modulo)    #dentro da variavel aulas , colocando facade.listar_aulas_de_modulos_ordenadas e passando modulo como parametro, ou seja ligando as aulas a seu respectivo modulo
    return render(request, 'modulos/modulo_detalhe.html',{'modulo': modulo, 'aulas': aulas})   #isto esta sendo aplicado em modulos/modulo_detalhe.html, e também passando o contexto

@login_required     #esse decorathor , esta dizendo que o login é obrigatório para ver os videos, ou seja o que esta no código abaixo
def aula(request, slug):                #vamos reenderizar o template com o contexto da aula passada aqui pelo slug
    aula = facade.encontrar_aula(slug)   #variavel aula = função facade.econtrar_aula passando slug como parametro
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})   #essa variavel sera usada dentro do template 'modulos/aula_detalhe.html'





