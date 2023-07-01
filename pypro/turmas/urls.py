from django.urls import path

from pypro.turmas import views

app_name = 'turmas'      #nome que aparecera no endereço da pagina, quando for chamado o indice.html
urlpatterns = [
    path('', views.indice, name='indice'),
]