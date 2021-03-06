# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HealthCheck.server_down'
        db.add_column(u'urlchecker_healthcheck', 'server_down',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'HealthCheck.status_code'
        db.alter_column(u'urlchecker_healthcheck', 'status_code', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'HealthCheck.server_down'
        db.delete_column(u'urlchecker_healthcheck', 'server_down')


        # User chose to not deal with backwards NULL issues for 'HealthCheck.status_code'
        raise RuntimeError("Cannot reverse this migration. 'HealthCheck.status_code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'HealthCheck.status_code'
        db.alter_column(u'urlchecker_healthcheck', 'status_code', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'urlchecker.healthcheck': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'HealthCheck'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server_down': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'status_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['urlchecker.Url']"})
        },
        u'urlchecker.url': {
            'Meta': {'object_name': 'Url'},
            'address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['urlchecker']