# Generated by Django 4.2.2 on 2023-06-26 01:10

from django.db import migrations
from django.utils.text import slugify

def popular_slug(apps, schrma_editor):
    Modulo = apps.get_model('modulos', 'Modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]