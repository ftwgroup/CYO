# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FeaturedBoxContent'
        db.create_table('content_featuredboxcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series_title', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('series_url', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date_descriptor', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('headliner', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('short_descriptor', self.gf('django.db.models.fields.TextField')()),
            ('poster_thumbnail', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
            ('tickets_url', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('content', ['FeaturedBoxContent'])


    def backwards(self, orm):
        
        # Deleting model 'FeaturedBoxContent'
        db.delete_table('content_featuredboxcontent')


    models = {
        'content.featuredboxcontent': {
            'Meta': {'object_name': 'FeaturedBoxContent'},
            'date_descriptor': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'headliner': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster_thumbnail': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            'series_title': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'series_url': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_descriptor': ('django.db.models.fields.TextField', [], {}),
            'tickets_url': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['content']
