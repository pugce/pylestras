from django.contrib import admin

from eventos.models import (Evento, Profile, Inscricao,
                            Palestra, Realizacao, Patrocinio)


class EventoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}
    list_display = ('titulo', 'data_realizacao', 'publicado')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


class PalestraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'evento')
    prepopulated_fields = {"slug": ("titulo",)}


class PatrocinioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato', 'tipo')


admin.site.register(Evento, EventoAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Palestra, PalestraAdmin)
admin.site.register(Patrocinio, PatrocinioAdmin)
admin.site.register(Inscricao)
admin.site.register(Realizacao)
