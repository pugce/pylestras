# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Palestra.horario'
        db.add_column('eventos_palestra', 'horario',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Palestra.horario'
        db.delete_column('eventos_palestra', 'horario')


    models = {
        'eventos.evento': {
            'Meta': {'ordering': "['-data_realizacao']", 'object_name': 'Evento'},
            'data_limite_inscricao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_realizacao': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limite_inscricoes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'local': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'patrocinadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['eventos.Patrocinio']", 'symmetrical': 'False'}),
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
            'horario': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palestrantes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['eventos.Profile']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
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
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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