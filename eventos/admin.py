#-*- coding: utf-8 -*-
from django.contrib import admin

from eventos.models import (Evento, Profile, Inscricao,
                            Palestra, Realizacao, Patrocinio)

class PalestraInline(admin.TabularInline):
    model = Palestra
    extra = 3

class EventoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                     {'fields': ['titulo']}),
        ('Informações sobre data', {'fields': ['data_realizacao'], 'classes': ['collapse']}),
    ]
    inlines = [PalestraInline]

    list_display = ('titulo', 'data_realizacao', 'publicado')
    list_filter = ['data_realizacao']
    search_fields = ['titulo'] # pode-se colocar mais de um, porém MAKE IT SIMPLE
    date_hierarchy = 'data_realizacao'


# class EventoAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("titulo",)}
#     list_display = ('titulo', 'data_realizacao', 'publicado')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


# class PalestraAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'evento')
#     prepopulated_fields = {"slug": ("titulo",)}


class PatrocinioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'tipo')


admin.site.register(Evento, EventoAdmin)
admin.site.register(Profile, ProfileAdmin)
#admin.site.register(Palestra, PalestraAdmin)
admin.site.register(Patrocinio, PatrocinioAdmin)
admin.site.register(Inscricao)
admin.site.register(Realizacao)
