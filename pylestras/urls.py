from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('eventos.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# TODO: definir como servir arquivos estaticos no heroku
urlpatterns += patterns('',
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.split('/'),
        'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT, 'show_indexes': False }),
    (r'^%s/(?P<path>.*)$' % settings.STATIC_URL.split('/'),
        'django.views.static.serve',
        { 'document_root': settings.STATIC_ROOT, 'show_indexes': False })
)
