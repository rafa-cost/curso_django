from typing import List

from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados pelo order
    :return:
    """

    return list(Modulo.objects.order_by('order').all()) #aqui estamos organizando a lista de modulos pelo "OrderedModel" e "move_up_down_links".


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)