from django.contrib import admin

from eventos.models import (Evento, Profile, Inscricao,
                            Palestra, Realizacao, Patrocinio)


class EventoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


admin.site.register(Evento, EventoAdmin)
admin.site.register(Profile)
admin.site.register(Inscricao)
admin.site.register(Palestra)
admin.site.register(Realizacao)
admin.site.register(Patrocinio)
