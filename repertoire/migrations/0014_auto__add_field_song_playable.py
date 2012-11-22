# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Song.playable'
        db.add_column('repertoire_song', 'playable', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Song.playable'
        db.delete_column('repertoire_song', 'playable')


    models = {
        'repertoire.concert': {
            'Meta': {'ordering': "['date_time']", 'object_name': 'Concert'},
            'abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'featured_artist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['repertoire.Performer']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'poster_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'program_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rough_date': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Series']", 'null': 'True', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Venue']", 'null': 'True'}),
            'video_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'repertoire.featuredartistinstrument': {
            'Meta': {'object_name': 'FeaturedArtistInstrument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Instrument']"}),
            'performed_song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.PerformedSong']"}),
            'performer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Performer']"})
        },
        'repertoire.guestartistinstrument': {
            'Meta': {'object_name': 'GuestArtistInstrument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Instrument']"}),
            'performed_song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.PerformedSong']"}),
            'performer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Performer']"})
        },
        'repertoire.instrument': {
            'Meta': {'object_name': 'Instrument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'repertoire.performedsong': {
            'Meta': {'object_name': 'PerformedSong'},
            'arranger': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'arranger'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'concert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Concert']", 'null': 'True', 'blank': 'True'}),
            'conductor': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'conductor'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'guest_artist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'guest_artist'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'premiere': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '1'}),
            'soloist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['repertoire.Performer']", 'null': 'True', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Song']"})
        },
        'repertoire.performer': {
            'Meta': {'object_name': 'Performer'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        'repertoire.soloistinstrument': {
            'Meta': {'object_name': 'SoloistInstrument'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrument': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Instrument']"}),
            'performed_song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.PerformedSong']"}),
            'performer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Performer']"})
        },
        'repertoire.song': {
            'Meta': {'object_name': 'Song'},
            'audio_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Performer']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        },
        'repertoire.venue': {
            'Meta': {'object_name': 'Venue'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['repertoire']
