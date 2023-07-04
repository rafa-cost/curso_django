from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_com_aulas()}  #acho que é uma lista de contexto
    return render(request, 'modulos/indice.html', ctx)   #criamos o endereço do nosso template, e depois passamos para o módulos urls
# Create your views here.
def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulos_ordenadas(modulo)  # essa parte estamos mostrando na pagina as aulas dos respectivos módulos, estamos importando de facade
    return render(request, 'modulos/modulo_detalhe.html',{'modulo': modulo, 'aulas': aulas})  # sera exibidas essas informações em modulos/modulo_detalhe.html

@login_required     #esse decorathor , esta dizendo que o login é obrigatório para ver os videos, ou seja o que esta no código abaixo
def aula(request, slug):
    aula = facade.encontrar_aula(slug)  #essa função encontrar_aula esta em modulo facade
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula}) #aqui estamos reenderizando para pagina modulos/aula_detalhe, ao clicarem nos links






