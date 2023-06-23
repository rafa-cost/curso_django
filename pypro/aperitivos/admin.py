from django.contrib.admin import ModelAdmin, register

from pypro.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id') #aqui estamos configurando dentro do djando admin
    ordering = ('creation',) #aqui estamos ordenando a ordem em que os videos irão aparecer, ele sera ordenado pela ordem de criação
    prepopulated_fields = {'slug':('titulo',)} #esse campo , ele automaticamente pega o que esta escrito no campo titulo, e passa para formatação de slug, no campo slug automaticamente