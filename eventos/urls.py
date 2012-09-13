from django.conf.urls import patterns, url

from eventos.views import EventoView


urlpatterns = patterns('',
    url(r'^evento/(?P<slug>[-\w]+)/$',
        EventoView.as_view(), name="evento_detail"),
)
