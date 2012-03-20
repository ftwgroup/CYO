# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'FeaturedBoxContent'
        db.delete_table('content_featuredboxcontent')


    def backwards(self, orm):
        
        # Adding model 'FeaturedBoxContent'
        db.create_table('content_featuredboxcontent', (
            ('headliner', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('short_descriptor', self.gf('django.db.models.fields.TextField')()),
            ('series_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('poster_thumbnail', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
            ('date_descriptor', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('series_title', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('content', ['FeaturedBoxContent'])


    models = {
        
    }

    complete_apps = ['content']
