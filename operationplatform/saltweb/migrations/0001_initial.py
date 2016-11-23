# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'userinfo'
        db.create_table(u'saltweb_userinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('updatetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'saltweb', ['userinfo'])

        # Adding model 'saltcommandhistory'
        db.create_table(u'saltweb_saltcommandhistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('minions', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('miniontype', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('module', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('arg', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'saltweb', ['saltcommandhistory'])

        # Adding model 'article'
        db.create_table(u'saltweb_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saltweb.userinfo'])),
            ('createtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('classify', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_stick', self.gf('django.db.models.fields.BooleanField')()),
            ('is_fine', self.gf('django.db.models.fields.BooleanField')()),
            ('answer', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('views', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('head_sculpture', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'saltweb', ['article'])


    def backwards(self, orm):
        # Deleting model 'userinfo'
        db.delete_table(u'saltweb_userinfo')

        # Deleting model 'saltcommandhistory'
        db.delete_table(u'saltweb_saltcommandhistory')

        # Deleting model 'article'
        db.delete_table(u'saltweb_article')


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
            'views': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
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