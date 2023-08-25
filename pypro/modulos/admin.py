from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modulos.models import Modulo, Aula


@admin.register(Modulo) #configurações dentro do admin do django, observamos que toda tabela criada, ele coloca o @admin.register
class ModuloAdmin(OrderedModelAdmin):         # o OrderedModel serve para organizar os modulos da forma que quisermos
    list_display = ('titulo', 'publico', 'move_up_down_links') #esse terceiro item é para organizar a ordem dos modulos, são as setinhas
    prepopulated_fields = {'slug': ('titulo',)} #esse campo , ele automaticamente pega o que esta escrito no campo titulo, e passa para formatação de slug, no campo slug automaticamente


@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'order', 'move_up_down_links')
    list_filter = ('modulo',)  #aqui estamos listando as aulas ao determinado módulo que ela pertence
    ordering = ('modulo', 'order') #vamos ordenar nossas aulas , primeiramente pela critério módulos e depois pelo parametro order. Conseguimos fazer isso, através das setinhas
    prepopulated_fields = {'slug': ('titulo',)}
