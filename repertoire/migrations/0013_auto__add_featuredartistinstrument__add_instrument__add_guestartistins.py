# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FeaturedArtistInstrument'
        db.create_table('repertoire_featuredartistinstrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Performer'])),
            ('performed_song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.PerformedSong'])),
            ('instrument', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Instrument'])),
        ))
        db.send_create_signal('repertoire', ['FeaturedArtistInstrument'])

        # Adding model 'Instrument'
        db.create_table('repertoire_instrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instrument', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('repertoire', ['Instrument'])

        # Adding model 'GuestArtistInstrument'
        db.create_table('repertoire_guestartistinstrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Performer'])),
            ('performed_song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.PerformedSong'])),
            ('instrument', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Instrument'])),
        ))
        db.send_create_signal('repertoire', ['GuestArtistInstrument'])

        # Adding model 'SoloistInstrument'
        db.create_table('repertoire_soloistinstrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('performer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Performer'])),
            ('performed_song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.PerformedSong'])),
            ('instrument', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Instrument'])),
        ))
        db.send_create_signal('repertoire', ['SoloistInstrument'])

        # Changing field 'Concert.description'
        db.alter_column('repertoire_concert', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Concert.series'
        db.alter_column('repertoire_concert', 'series_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Series'], null=True))

        # Changing field 'Concert.abstract'
        db.alter_column('repertoire_concert', 'abstract', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Concert.season'
        db.alter_column('repertoire_concert', 'season', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Song.description'
        db.alter_column('repertoire_song', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Venue.city'
        db.alter_column('repertoire_venue', 'city', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Venue.address1'
        db.alter_column('repertoire_venue', 'address1', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Venue.state'
        db.alter_column('repertoire_venue', 'state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2, null=True))

        # Changing field 'Venue.zip_code'
        db.alter_column('repertoire_venue', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'PerformedSong.concert'
        db.alter_column('repertoire_performedsong', 'concert_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Concert'], null=True))

        # Changing field 'Performer.bio'
        db.alter_column('repertoire_performer', 'bio', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Performer.birth_year'
        db.alter_column('repertoire_performer', 'birth_year', self.gf('django.db.models.fields.IntegerField')(null=True))


    def backwards(self, orm):
        
        # Deleting model 'FeaturedArtistInstrument'
        db.delete_table('repertoire_featuredartistinstrument')

        # Deleting model 'Instrument'
        db.delete_table('repertoire_instrument')

        # Deleting model 'GuestArtistInstrument'
        db.delete_table('repertoire_guestartistinstrument')

        # Deleting model 'SoloistInstrument'
        db.delete_table('repertoire_soloistinstrument')

        # Changing field 'Concert.description'
        db.alter_column('repertoire_concert', 'description', self.gf('django.db.models.fields.TextField')(default='No description'))

        # Changing field 'Concert.series'
        db.alter_column('repertoire_concert', 'series_id', self.gf('django.db.models.fields.related.ForeignKey')(default='No series', to=orm['repertoire.Series']))

        # Changing field 'Concert.abstract'
        db.alter_column('repertoire_concert', 'abstract', self.gf('django.db.models.fields.TextField')(default='No abstract'))

        # Changing field 'Concert.season'
        db.alter_column('repertoire_concert', 'season', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Song.description'
        db.alter_column('repertoire_song', 'description', self.gf('django.db.models.fields.TextField')(default='No description'))

        # Changing field 'Venue.city'
        db.alter_column('repertoire_venue', 'city', self.gf('django.db.models.fields.CharField')(default='No city', max_length=60))

        # Changing field 'Venue.address1'
        db.alter_column('repertoire_venue', 'address1', self.gf('django.db.models.fields.CharField')(default='No address', max_length=64))

        # Changing field 'Venue.state'
        db.alter_column('repertoire_venue', 'state', self.gf('django.contrib.localflavor.us.models.USStateField')(default='Oh', max_length=2))

        # Changing field 'Venue.zip_code'
        db.alter_column('repertoire_venue', 'zip_code', self.gf('django.db.models.fields.CharField')(default=45247, max_length=10))

        # Changing field 'PerformedSong.concert'
        db.alter_column('repertoire_performedsong', 'concert_id', self.gf('django.db.models.fields.related.ForeignKey')(default='No concert', to=orm['repertoire.Concert']))

        # Changing field 'Performer.bio'
        db.alter_column('repertoire_performer', 'bio', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Performer.birth_year'
        db.alter_column('repertoire_performer', 'birth_year', self.gf('django.db.models.fields.IntegerField')(default=9999))


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
