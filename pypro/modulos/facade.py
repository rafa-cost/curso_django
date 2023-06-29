from typing import List

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados pelo order
    :return:
    """

    return list(Modulo.objects.order_by('order').all())  # aqui estamos organizando a lista de modulos pelo "OrderedModel" e "move_up_down_links".


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulos_ordenadas(modulo: Modulo): #listando as aulas de cada módulos
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.get(slug=slug)   #no meu entender estamos aqui pegando o slug do banco de dados, para transformar os titulos em links