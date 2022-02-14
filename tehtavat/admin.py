from django.contrib import admin

from .models import Kategoria, Tehtava


@admin.register(Tehtava)
class TehtavaAdmin(admin.ModelAdmin):
    list_display = ["id", "otsikko", "kategoria"]


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    pass
