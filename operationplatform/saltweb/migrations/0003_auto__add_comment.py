# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'comment'
        db.create_table(u'saltweb_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saltweb.userinfo'])),
            ('articlename', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saltweb.article'])),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'saltweb', ['comment'])


    def backwards(self, orm):
        # Deleting model 'comment'
        db.delete_table(u'saltweb_comment')


    models = {
        u'saltweb.article': {
            'Meta': {'object_name': 'article'},
            'answer': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['saltweb.userinfo']"}),
            'classify': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head_sculpture': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_fine': ('django.db.models.fields.BooleanField', [], {}),
            'is_stick': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_home': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'views': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'saltweb.comment': {
            'Meta': {'object_name': 'comment'},
            'articlename': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['saltweb.article']"}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['saltweb.userinfo']"})
        },
        u'saltweb.saltcommandhistory': {
            'Meta': {'object_name': 'saltcommandhistory'},
            'arg': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minions': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'miniontype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'saltweb.userinfo': {
            'Meta': {'object_name': 'userinfo'},
            'createtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updatetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['saltweb']