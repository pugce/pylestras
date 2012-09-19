from eventos.models import Evento


def eventos(request):
    return {
        'eventos': Evento.publicados.all(),
    }
