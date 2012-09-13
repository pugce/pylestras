from django.views.generic import DetailView

from eventos.models import Evento, Palestra

class EventoView(DetailView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        context['palestras'] = Palestra.objects.filter(evento__slug=self.kwargs['slug'])
        return context
