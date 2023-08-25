"""
URL configuration for pypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from pypro.base.views import home

urlpatterns = [
    path('admin/', admin.site.urls),      #endereço do django admin
    path('contas/', include('django.contrib.auth.urls')),    #contas/login para o usuario se logar no site
    path('', include('pypro.base.urls')),                    #a pagina home do projeto
    path('aperitivos/', include('pypro.aperitivos.urls')),   #abaixo seus aplicativos
    path('modulos/', include('pypro.modulos.urls')),
    path('turmas/', include('pypro.turmas.urls')),
]

if settings.DEBUG:
    import debug_toolbar  # é a barra de ferramenta que fica do lado direito da pagina

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
