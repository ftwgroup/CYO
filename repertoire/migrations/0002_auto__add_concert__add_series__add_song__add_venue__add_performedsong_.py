# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Concert'
        db.create_table('repertoire_concert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Series'])),
            ('season', self.gf('django.db.models.fields.IntegerField')()),
            ('rough_date', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Venue'], null=True)),
            ('poster', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('media_link', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('repertoire', ['Concert'])

        # Adding M2M table for field featured_artist on 'Concert'
        db.create_table('repertoire_concert_featured_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('concert', models.ForeignKey(orm['repertoire.concert'], null=False)),
            ('performer', models.ForeignKey(orm['repertoire.performer'], null=False))
        ))
        db.create_unique('repertoire_concert_featured_artist', ['concert_id', 'performer_id'])

        # Adding model 'Series'
        db.create_table('repertoire_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('repertoire', ['Series'])

        # Adding model 'Song'
        db.create_table('repertoire_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('composer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Performer'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('repertoire', ['Song'])

        # Adding model 'Venue'
        db.create_table('repertoire_venue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('repertoire', ['Venue'])

        # Adding model 'PerformedSong'
        db.create_table('repertoire_performedsong', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Song'])),
            ('concert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['repertoire.Concert'])),
            ('premiere', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('repertoire', ['PerformedSong'])

        # Adding M2M table for field arranger on 'PerformedSong'
        db.create_table('repertoire_performedsong_arranger', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performedsong', models.ForeignKey(orm['repertoire.performedsong'], null=False)),
            ('performer', models.ForeignKey(orm['repertoire.performer'], null=False))
        ))
        db.create_unique('repertoire_performedsong_arranger', ['performedsong_id', 'performer_id'])

        # Adding M2M table for field conductor on 'PerformedSong'
        db.create_table('repertoire_performedsong_conductor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performedsong', models.ForeignKey(orm['repertoire.performedsong'], null=False)),
            ('performer', models.ForeignKey(orm['repertoire.performer'], null=False))
        ))
        db.create_unique('repertoire_performedsong_conductor', ['performedsong_id', 'performer_id'])

        # Adding M2M table for field guest_artist on 'PerformedSong'
        db.create_table('repertoire_performedsong_guest_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performedsong', models.ForeignKey(orm['repertoire.performedsong'], null=False)),
            ('performer', models.ForeignKey(orm['repertoire.performer'], null=False))
        ))
        db.create_unique('repertoire_performedsong_guest_artist', ['performedsong_id', 'performer_id'])

        # Adding M2M table for field soloist on 'PerformedSong'
        db.create_table('repertoire_performedsong_soloist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performedsong', models.ForeignKey(orm['repertoire.performedsong'], null=False)),
            ('performer', models.ForeignKey(orm['repertoire.performer'], null=False))
        ))
        db.create_unique('repertoire_performedsong_soloist', ['performedsong_id', 'performer_id'])

        # Adding model 'Performer'
        db.create_table('repertoire_performer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('birth_year', self.gf('django.db.models.fields.IntegerField')()),
            ('death_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('repertoire', ['Performer'])


    def backwards(self, orm):
        
        # Deleting model 'Concert'
        db.delete_table('repertoire_concert')

        # Removing M2M table for field featured_artist on 'Concert'
        db.delete_table('repertoire_concert_featured_artist')

        # Deleting model 'Series'
        db.delete_table('repertoire_series')

        # Deleting model 'Song'
        db.delete_table('repertoire_song')

        # Deleting model 'Venue'
        db.delete_table('repertoire_venue')

        # Deleting model 'PerformedSong'
        db.delete_table('repertoire_performedsong')

        # Removing M2M table for field arranger on 'PerformedSong'
        db.delete_table('repertoire_performedsong_arranger')

        # Removing M2M table for field conductor on 'PerformedSong'
        db.delete_table('repertoire_performedsong_conductor')

        # Removing M2M table for field guest_artist on 'PerformedSong'
        db.delete_table('repertoire_performedsong_guest_artist')

        # Removing M2M table for field soloist on 'PerformedSong'
        db.delete_table('repertoire_performedsong_soloist')

        # Deleting model 'Performer'
        db.delete_table('repertoire_performer')


    models = {
        'repertoire.concert': {
            'Meta': {'object_name': 'Concert'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured_artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['repertoire.Performer']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_link': ('django.db.models.fields.TextField', [], {}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'rough_date': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Series']"}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Venue']", 'null': 'True'})
        },
        'repertoire.performedsong': {
            'Meta': {'object_name': 'PerformedSong'},
            'arranger': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'arranger'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'concert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['repertoire.Concert']"}),
            'conductor': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'conductor'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'guest_artist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'guest_artist'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['repertoire.Performer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'premiere': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
