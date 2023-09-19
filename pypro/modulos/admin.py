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
    list_filter = ('modulo',)  #aqui esttamos fazendo um filtro para ver o modulo com a suas respectivas aulas
    ordering = ('modulo', 'order') #vamos ordenar pelos modulos e dentro dos modulos pelo order
    prepopulated_fields = {'slug': ('titulo',)}
