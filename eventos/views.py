from django.views.generic import DetailView
from django.http import Http404

from eventos.models import Evento, Palestra

class EventoView(DetailView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        context['palestras'] = Palestra.objects.filter(evento__slug=self.kwargs['slug'])
        return context


class EventoAtualView(EventoView):

    def get_object(self, queryset=None):
        try:
            evento = Evento.publicados.latest()
        except Evento.DoesNotExist:
            raise Http404
        self.kwargs['slug'] = evento.slug
        return evento
