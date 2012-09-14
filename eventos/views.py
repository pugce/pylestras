from django.views.generic import DetailView
from django.http import Http404

from eventos.models import Evento, Palestra, Patrocinio
from eventos.models import PA_FINANCEIRO, PA_REALIZACAO

class EventoView(DetailView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        context['palestras'] = Palestra.objects.filter(evento__slug=self.kwargs['slug'])
        #TODO: as consultas abaixo nao trazem resultado real para multiplos eventos
        # necessario refatorar os modelos.
        context['patrocinio'] = Patrocinio.objects.filter(tipo=PA_FINANCEIRO)
        context['apoio'] = Patrocinio.objects.exclude(tipo__in=[PA_FINANCEIRO, PA_REALIZACAO])
        context['realizacao'] = Patrocinio.objects.filter(tipo=PA_REALIZACAO)
        return context


class EventoAtualView(EventoView):

    def get_object(self, queryset=None):
        try:
            evento = Evento.publicados.latest()
        except Evento.DoesNotExist:
            raise Http404
        self.kwargs['slug'] = evento.slug
        return evento
