from django.urls import path

from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),    #quando acessado aqui mostra o modulo/slug do modulo
    path('aulas/<slug:slug>', views.aula, name='aula'),   #aqui mostra modulos/aulas/slug da aula
    path('', views.indice, name='indice'), #string vazia para bater na raiz do projeto, ou seja pagina principal

]