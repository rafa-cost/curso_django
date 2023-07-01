from django.contrib import admin

from pypro.turmas.models import Turma

class MatriculaInline(admin.TabularInline):   #esse tabular é para deixar o formulário em forma horizontal de linha, e não as informações uma embaixo da outra
    model = Turma.alunos.through
    extra = 1           #é para aperecer um formulário por vez, pq o padrão é aparecer 3 de inicio
    readonly_fields = ('data',)     #campo somente de leitura , não da para alterar, nesse caso mostra a data
    autocomplete_fields = ('usuario',)     #esse campo vai fazendo o autocomplete dos emails dos ususarios , que estão registrados no bando de dados
    ordering = ('-data',)      #estamos organizando o campo de data pela ordem decrescente, no campo de cadastro de alunos.
# Register your models here.

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)









