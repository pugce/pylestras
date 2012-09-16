#-*- coding: utf-8 -*-
from django.contrib import admin

from eventos.models import (Evento, Profile, Inscricao,
                            Palestra, Realizacao, Patrocinio)

class PalestraInline(admin.TabularInline):
    model = Palestra
    prepopulated_fields = { 'slug': ('titulo',)}
    extra = 1


class EventoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    fieldsets = [
        (None,                           {'fields': ['titulo']}),
        ('Publicado?',                   {'fields': ['publicado']}),
        ('Slug',                         {'fields': ['slug']}),
        ('Informações sobre data',       {'fields': ['data_realizacao'], 'classes': ['collapse']}),
        ('Informações sobre o evento',   {'fields': ['local', 'descricao'], 'classes': ['collapse']}),
        ('Informações sobre inscricoes', {'fields': ['valor', 'data_limite_inscricao', 'limite_inscricoes'], 'classes': ['collapse']}),
        ('Patrocinadores',               {'fields': ['patrocinadores'], 'classes': ['collapse']}),
    ]
    inlines = [PalestraInline]

    list_display = ('titulo', 'data_realizacao', 'publicado')
    list_filter = ['data_realizacao']
    search_fields = ['titulo'] # pode-se colocar mais de um, porém MAKE IT SIMPLE
    date_hierarchy = 'data_realizacao'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


class PatrocinioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'tipo')


admin.site.register(Evento, EventoAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Patrocinio, PatrocinioAdmin)
admin.site.register(Inscricao)
admin.site.register(Realizacao)
