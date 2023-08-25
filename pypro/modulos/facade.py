from typing import List

from django.db.models import Prefetch

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados pelo order
    :return:
    """

    return list(Modulo.objects.order_by('order').all())  # aqui estamos organizando a lista de modulos pelo "OrderedModel" e "move_up_down_links".


def encontrar_modulo(slug: str) -> Modulo:    #encontrar modulo, também tem a ver com a pagina modulo_detalhe.html, que seria para exibir o modulo individualmente
    return Modulo.objects.get(slug=slug)

def listar_aulas_de_modulos_ordenadas(modulo: Modulo):    #é referente a pagina modulo_detalhe.html, ou seja essa pagina exibe o modulo individualmente com seus videos
    return list(modulo.aula_set.order_by('order').all())

def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)   #aqui é para pagina aula.html, a pagina que exibe os videos, assim que selecionados

def listar_modulos_com_aulas():   #aqui ira mostrar todos os modulos com sua respectivas aulas, no indice.html
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')).all()







