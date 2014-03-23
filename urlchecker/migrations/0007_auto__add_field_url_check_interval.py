# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Url.check_interval'
        db.add_column(u'urlchecker_url', 'check_interval',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Url.check_interval'
        db.delete_column(u'urlchecker_url', 'check_interval')


    models = {
        u'urlchecker.healthcheck': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'HealthCheck'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'time': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['urlchecker.Url']"})
        },
        u'urlchecker.url': {
            'Meta': {'object_name': 'Url'},
            'address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'check_interval': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['urlchecker']