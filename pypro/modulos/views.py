from django.shortcuts import render

from pypro.modulos import facade


# Create your views here.
def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulos_ordenadas(modulo)  # essa parte estamos mostrando na pagina as aulas dos respectivos módulos, estamos importando de facade
    return render(request, 'modulos/modulo_detalhe.html',{'modulo': modulo, 'aulas': aulas})  # sera exibidas essas informações em modulos/modulo_detalhe.html


def aula(request, slug):
    aula = facade.encontrar_aula(slug)  #essa função encontrar_aula esta em modulo facade
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula}) #aqui estamos reenderizando para pagina modulos/aula_detalhe, ao clicarem nos links
