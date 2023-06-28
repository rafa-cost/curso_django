from pypro.modulos import facade


def listar_modulos(request):
    return {'MODULOS': facade.listar_modulos_ordenados()} #esse código no meu intender, é para que o botão modulos esteja em todas as paginas do site, inclusive adicionamos um codigo no template do settings
