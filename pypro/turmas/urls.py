from django.urls import path

from pypro.turmas import views

app_name = 'turmas'      #nome do aplicativo
urlpatterns = [
    path('', views.indice, name='indice'),
]