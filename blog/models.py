# -*- coding:utf-8 -*-
from django.db import models
from eventos.models import Profile
from taggit.managers import TaggableManager


class PublicacaoManager(models.Manager):
    def get_query_set(self):
        return super(PublicoManager, self).get_query_set().filter(publicado=True)


class Postagem(models.Model):
    publicado = models.BooleanField('Publicado?', default=False)
    publicacao = models.DateTimeField('Data de publicação', editable=False, blank=True, null=True)
    modificacao = models.DateTimeField('Data da última modificação', auto_now=True)
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    texto = models.TextField()
    html = models.TextField(editable=False)
    diff = models.TextField(editable=False)
    autor = models.ForeignKey(Profile)
    tags = TaggableManager(blank=True)

    objects = models.Manager()
    publicados = PublicacaoManager()

    class Meta:
        verbose_name_plural = 'Postagens'

    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', [self.slug])
