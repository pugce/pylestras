from django.conf.urls import patterns, url

from eventos.views import EventoView, EventoAtualView


urlpatterns = patterns('',
    url(r'', EventoAtualView.as_view(), name='evento_index'),
    url(r'^evento/(?P<slug>[-\w]+)/$',
        EventoView.as_view(), name="evento_detail"),
)
