"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from eventos.models import Evento, Patrocinio
from django.core.urlresolvers import reverse


class EventoTestCase(TestCase):
    fixtures = ['evento_testdata.json']

    def setUp(self):
        super(EventoTestCase, self).setUp()
        self.evento_1 = Evento.objects.get(pk=1)
        self.evento_3 = Evento.objects.get(pk=3)

    def test_unicode(self):
        self.assertEqual(self.evento_1.__unicode__(), self.evento_1.titulo)

    def test_get_absolute_url(self):
        url = reverse('evento_detail', args=[self.evento_1.slug])
        self.assertEqual(self.evento_1.get_absolute_url(), url)

    def test_se_evento_foi_publicado(self):
        self.assertTrue(self.evento_1.publicado)
        self.assertFalse(self.evento_3.publicado)
