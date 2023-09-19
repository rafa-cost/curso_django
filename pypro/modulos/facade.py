from typing import List

from django.db.models import Prefetch

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:   #aqui acho que tem haver que quando clicamos no botão , aparecem os modulos, um embaixo do outro, ou seja uma lista. E esta lista esta sendo ordenada pelo "order", definimos assim no models. order são as setinhas que estão na parte do django admin, onde podemos mudar de posição os modulos
    """
    Lista módulos ordenados pelo order
    :return:
    """

    return list(Modulo.objects.order_by('order').all()) #aqui esta dizendo que a lista de objetos de Modulo esta sendo organizada pelo order(dentro do banco de dados)


def encontrar_modulo(slug: str) -> Modulo:  #estamos definindo aqui que o tipo do slug sera uma string, e nós vamos retornar aqui como execução da faixada um modulo
    return Modulo.objects.get(slug=slug)     #aqui no caso , ele é usado nas pagina modulo_detalhe.html para mostrar o titulo do modulo, descrição do módulo e publico do módulo
                                            #para retornar o modulo a partir do slug, o slug recebido como parametro tera que ser igual a slug do Modulo(models), ou seja para pegar o módulo que o usuario escolheu
def listar_aulas_de_modulos_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())  #essa função esta guardando os nomes das aulas , ela lista os nomes das aulas de cada modulo
                                                          #esse aula_set é criada por conta da chave estrangeira no relacionamento de muitos para 1, a classe que esta recebendo a chave estrangeira vai ter "nome da classe_set". Que aqui no caso ira listar todas as aulas de cada modulo
                                                          ##apartir do meu objeto modulo vou acessar aula_set, vamos ordenar as aulas pelo atributo order, pegando todas as aulas com o "all". Passando essas informaçõe para uma lista "list".
def encontrar_aula(slug):                                        # essa função ela guarda os videos das aulas
    return Aula.objects.select_related('modulo').get(slug=slug)   #aqui esta pegando os videos da tabela Aula no bando de dados, as aulas ordenadas pelo modulo. Vamos pegar a aula respectiva a seu slug
                                                                  #select_related é uma ferramenta do objects que faz uma busca mais especifica e rapida. select_related só pode ser usado do lado de quem recebe a chave estrangeira, do outro lado que esta fornecendo o campo teriaque usar o prefetch_related, como esta na função abaixo
def listar_modulos_com_aulas():     # a função aqui ela faz uma lista com todos os modulos e suas respectivas aulas
    aulas_ordenadas = Aula.objects.order_by('order')    #aqui a variavel esta pegando as aulas ordenadas de tabela Aula no bando de dados
    return Modulo.objects.order_by('order').prefetch_related(Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')).all()   #pegando o modulo no banco de dados e fazendo ligação do modulo com suas respectivas aulas
                                                         # esse aula_set é criada por conta da chave estrangeira no relacionamento de muitos para 1, a classe que esta recebendo a chave estrangeira vai ter "nome da classe_set". Que aqui no caso ira listar todas as aulas de cada modulo
                                                         #prefetch_related é uma ferramenta do obejcts ele é primo do select_related. Só que tem uma diferença o select_related é usado do lado de quem recebe a chave estrangeira. Agora quem fornece o campo de dados, tem que usar o prefect_related. Ambos servem para fazer buscas mais especificas e menos burocraticas, tornando o programa mais rapido e eficaz.
                                                         #esse Prefetch, ele permiti que vc melhore a configuração do prefect_related




