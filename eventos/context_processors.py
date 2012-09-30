from eventos.models import Evento


def eventos(request):
    evento_list = Evento.publicados.all()
    ultima_versao = str(evento_list.latest())[0]
    return {
        'eventos': evento_list,
        'ultima_versao': ultima_versao,
    }
