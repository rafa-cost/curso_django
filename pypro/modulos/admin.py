from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modulos.models import Modulo


@admin.register(Modulo) #configurações dentro do admin do django
class ModuloAdmin(OrderedModelAdmin):         # o OrderedModel serve para organizar os modulos da forma que quisermos
    list_display = ('titulo', 'publico', 'move_up_down_links') #esse terceiro item é para organizar a ordem dos modulos
    prepopulated_fields = {'slug': ('titulo',)} #esse campo , ele automaticamente pega o que esta escrito no campo titulo, e passa para formatação de slug, no campo slug automaticamente
