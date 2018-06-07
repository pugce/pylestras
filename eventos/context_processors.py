from eventos.models import Evento


def eventos(request):
    evento_list = Evento.publicados.all()

    try:
        ultima_versao = evento_list.latest().titulo.split()[0]
    except:
        ultima_versao = None
    return {
        'eventos': evento_list,
        'ultima_versao': ultima_versao,
    }
