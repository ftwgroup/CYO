# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Venue.title'
        db.delete_column('repertoire_venue', 'title')

        # Adding field 'Venue.name'
        db.add_column('repertoire_venue', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Venue.title'
        db.add_column('repertoire_venue', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=128), keep_default=False)

        # Deleting field 'Venue.name'
        db.delete_column('repertoire_venue', 'name')


    models = {
        'repertoire.concert': {
            'Meta': {'ordering': "['date_time']", 'object_name': 'Concert'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured_artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['repertoire.Performer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'poster_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'program_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rough_date': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Series']"}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Venue']", 'null': 'True'}),
            'video_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'repertoire.performedsong': {
            'Meta': {'object_name': 'PerformedSong'},
            'arranger': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'arranger'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'concert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Concert']"}),
            'conductor': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'conductor'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'guest_artist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'guest_artist'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'premiere': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'soloist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['repertoire.Performer']", 'null': 'True', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Song']"})
        },
        'repertoire.performer': {
            'Meta': {'object_name': 'Performer'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'repertoire.series': {
            'Meta': {'object_name': 'Series'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'repertoire.song': {
            'Meta': {'object_name': 'Song'},
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Performer']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        },
        'repertoire.venue': {
            'Meta': {'object_name': 'Venue'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['repertoire']
