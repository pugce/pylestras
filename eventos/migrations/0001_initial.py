# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Evento'
        db.create_table('eventos_evento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publicado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_realizacao', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('local', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
            ('data_limite_inscricao', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('limite_inscricoes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('eventos', ['Evento'])

        # Adding model 'Profile'
        db.create_table('eventos_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('github', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('bitbucket', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('cv', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('eventos', ['Profile'])

        # Adding model 'Inscricao'
        db.create_table('eventos_inscricao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='inscritos', to=orm['eventos.Evento'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Profile'])),
            ('valor', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('pagamento', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('data_pagamento', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('data_inscricao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('eventos', ['Inscricao'])

        # Adding model 'Palestra'
        db.create_table('eventos_palestra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('eventos', ['Palestra'])

        # Adding M2M table for field palestrantes on 'Palestra'
        db.create_table('eventos_palestra_palestrantes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('palestra', models.ForeignKey(orm['eventos.palestra'], null=False)),
            ('profile', models.ForeignKey(orm['eventos.profile'], null=False))
        ))
        db.create_unique('eventos_palestra_palestrantes', ['palestra_id', 'profile_id'])

        # Adding model 'Realizacao'
        db.create_table('eventos_realizacao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento'])),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Profile'])),
        ))
        db.send_create_signal('eventos', ['Realizacao'])

        # Adding model 'Patrocinio'
        db.create_table('eventos_patrocinio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('valor', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('contato', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('banner', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('eventos', ['Patrocinio'])


    def backwards(self, orm):
        # Deleting model 'Evento'
        db.delete_table('eventos_evento')

        # Deleting model 'Profile'
        db.delete_table('eventos_profile')

        # Deleting model 'Inscricao'
        db.delete_table('eventos_inscricao')

        # Deleting model 'Palestra'
        db.delete_table('eventos_palestra')

        # Removing M2M table for field palestrantes on 'Palestra'
        db.delete_table('eventos_palestra_palestrantes')

        # Deleting model 'Realizacao'
        db.delete_table('eventos_realizacao')

        # Deleting model 'Patrocinio'
        db.delete_table('eventos_patrocinio')


    models = {
        'eventos.evento': {
            'Meta': {'ordering': "['-data_realizacao']", 'object_name': 'Evento'},
            'data_limite_inscricao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_realizacao': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limite_inscricoes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'local': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'})
        },
        'eventos.inscricao': {
            'Meta': {'object_name': 'Inscricao'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'data_inscricao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_pagamento': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscritos'", 'to': "orm['eventos.Evento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pagamento': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventos.Profile']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'eventos.palestra': {
            'Meta': {'object_name': 'Palestra'},
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventos.Evento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palestrantes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['eventos.Profile']", 'symmetrical': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eventos.patrocinio': {
            'Meta': {'object_name': 'Patrocinio'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contato': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'})
        },
        'eventos.profile': {
            'Meta': {'object_name': 'Profile'},
            'bitbucket': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'eventos.realizacao': {
            'Meta': {'object_name': 'Realizacao'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventos.Evento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventos.Profile']"})
        }
    }

    complete_apps = ['eventos']