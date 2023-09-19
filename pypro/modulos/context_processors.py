from pypro.modulos import facade


def listar_modulos(request):
    return {'MODULOS': facade.listar_modulos_ordenados()} #esse código , é para que o botão modulos esteja presente em todas as paginas do site, sem que eu precise colocar esta variavel (MODULOS) em todas as viwes. Por isso fizemos esse context_processors, inclusive adicionamos um codigo no template do settings
                                                          #essa variavel MODULOS é usada no base.html