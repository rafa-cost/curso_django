from django.urls import path

from pypro.aperitivos.views import video, indice

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),  #quando coloca /aperitivos no endereço da pagina , direciona para indice
]
