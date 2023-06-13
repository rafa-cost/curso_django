from django.shortcuts import render

from pypro.diango_assertions import assert_contains


def video(request, slug):
    return render(request, 'aperitivos/video.html')  #módulo views tem ligação diretamente com o modulo urls



