from django.urls import path

from pypro.aperitivos.views import video, indice

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),   #quando o video é selecionado na pagina de indice, ira para a pagina de video, assim aparecera na barra de endereço aperitivos/slug do video
    path('', indice, name='indice'),  #quando coloca /aperitivos no endereço da pagina , direciona para indice.html
]
