# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


STPG_PAGO, STPG_PENDENTE, STPG_CORTESIA = True, False, None

CHOICES_STATUS_PAGAMENTO = (
    (STPG_PAGO, 'pago'),
    (STPG_PENDENTE, 'pendente'),
    (STPG_CORTESIA, 'cortesia'),
)

PA_FINANCEIRO, PA_SERVICO, PA_DOACAO, PA_APOIO, PA_REALIZACAO, PA_SORTEIO, PA_OUTRO = 0, 1, 2, 3, 4, 5, 6

CHOICES_TIPO_PATROCINIO = (
    (PA_FINANCEIRO, 'financeiro'),
    (PA_SERVICO, 'serviço'),
    (PA_DOACAO, 'doação'),
    (PA_APOIO, 'apoio'),
    (PA_REALIZACAO, 'realização'),
    (PA_SORTEIO, 'sorteio'),
    (PA_OUTRO, 'outro'),
)


class PublicoManager(models.Manager):
    def get_query_set(self):
        query_set = super(PublicoManager, self).get_query_set()
        query_set = query_set.filter(publicado=True)
        return query_set


class Evento(models.Model):
    publicado = models.BooleanField('Publicar?', default=False)
    data_realizacao = models.DateTimeField('Data de realização', blank=True, null=True)
    local = models.TextField('Local de realização', blank=True, null=True)
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField(max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)
    valor = models.DecimalField(default=0, max_digits=8, decimal_places=2,
                                help_text='Em reais (R$)')
    data_limite_inscricao = models.DateField(blank=True, null=True)
    limite_inscricoes = models.PositiveIntegerField('Limite de inscrições', blank=True, null=True)
    patrocinadores = models.ManyToManyField('Patrocinio', verbose_name='Patrocínios')

    objects = models.Manager()
    publicados = PublicoManager()

    class Meta:
        get_latest_by = 'data_realizacao'
        ordering = ['-data_realizacao']

    def get_absolute_url(self):
        return reverse('evento_detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo


class Profile(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    site = models.URLField(blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    bitbucket = models.URLField(blank=True, null=True)
    cv = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.nome


class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, related_name='inscritos')
    profile = models.ForeignKey(Profile)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    pagamento = models.NullBooleanField(choices=CHOICES_STATUS_PAGAMENTO)
    data_pagamento = models.DateTimeField(blank=True, null=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=12)

    def __unicode__(self):
        return u'Inscrição %05d' % self.id


class Palestra(models.Model):
    evento = models.ForeignKey(Evento)
    palestrantes = models.ManyToManyField(Profile)
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField(max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('palestra_detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo


class Realizacao(models.Model):
    '''
    Responsáveis pela organização do evento.
    '''
    evento = models.ForeignKey(Evento)
    profile = models.ForeignKey(Profile)

    def __unicode__(self):
        return u'%s' % self.profile


class Patrocinio(models.Model):
    tipo = models.IntegerField(choices=CHOICES_TIPO_PATROCINIO)
    valor = models.DecimalField(default=0, max_digits=8, decimal_places=2,
                                help_text='Em reais (R$)')
    descricao = models.TextField('Descrição',
                                 help_text='Caso não seja financeiro',
                                 blank=True, null=True)
    contato = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    banner = models.ImageField(upload_to='banners', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    texto = models.TextField(help_text='Caso solicitado', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.nome or self.contato)
