from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import redirect

from eventos.models import Evento, Palestra, Profile
from eventos.models import PA_FINANCEIRO, PA_REALIZACAO


class EventoView(DetailView):
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoView, self).get_context_data(**kwargs)
        evento = self.object
        context['palestras'] = evento.palestra_set.all().prefetch_related('palestrantes')
        context['patrocinio'] = evento.patrocinadores.filter(tipo=PA_FINANCEIRO)
        context['apoio'] = evento.patrocinadores.exclude(tipo__in=[PA_FINANCEIRO, PA_REALIZACAO])
        context['realizacao'] = evento.patrocinadores.filter(tipo=PA_REALIZACAO)
        return context


class EventoAtualView(EventoView):

    def get_object(self, queryset=None):
        try:
            evento = Evento.publicados.latest()
        except Evento.DoesNotExist:
            raise Http404
        self.kwargs['slug'] = evento.slug
        return evento


class PalestraDetailView(DetailView):
    model = Palestra


class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        profile = self.object
        context['palestras'] = profile.palestra_set.all()
        return context


def view_lastest_event(request):
    try:
        return redirect(Evento.publicados.latest())
    except:
        raise Http404()