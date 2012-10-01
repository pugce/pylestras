from django.conf.urls import patterns, url

from eventos.views import (EventoView, EventoAtualView, PalestraDetailView,
                           ProfileDetailView)


urlpatterns = patterns('',
    url(r'^$', 'eventos.views.view_lastest_event', name='evento_index'),
    url(r'^evento/(?P<slug>[-\w]+)/$',
        EventoView.as_view(), name="evento_detail"),
    url(r'^palestra/(?P<slug>[-\w]+)/$',
        PalestraDetailView.as_view(), name="palestra_detail"),
    url(r'^profile/(?P<pk>\d+)/$',
        ProfileDetailView.as_view(), name="profile_detail"),

)
