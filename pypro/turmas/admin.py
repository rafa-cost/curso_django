from django.contrib import admin

from pypro.turmas.models import Turma
# essa classe vai gerar o campo matricula para adicionar usuario. No admin do django
class MatriculaInline(admin.TabularInline):   #esse tabular é para deixar o formulário em forma horizontal de linha, e não as informações uma embaixo da outra
    model = Turma.alunos.through     #no banco vamos acessar Turma, campo aluno, e nesse campo temos "througth" que é justamente o acesso a tabela intermediaria
    extra = 1           #é para aperecer um formulário por vez, pq o padrão é aparecer 3 de inicio
    readonly_fields = ('data',)     #campo somente de leitura , não da para alterar, nesse caso mostra a data
    autocomplete_fields = ('usuario',)     #esse campo vai fazendo o autocomplete dos emails dos ususarios , que estão registrados no bando de dados, ao vc ir digitando ja aparece o email referente a digitação
    ordering = ('-data',)      #estamos organizando o campo de data pela ordem decrescente, no campo de cadastro de alunos.
# Register your models here.

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]       # aqui estamos indicando a lista de inlines que esta acima
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)









