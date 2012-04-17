# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('page_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150, db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['page.Page'])),
            ('in_navigation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('override_url', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('redirect_to', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('_cached_url', self.gf('django.db.models.fields.CharField')(default='', max_length=300, db_index=True, blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 4, 17, 14, 55))),
            ('publication_end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('navigation_extension', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_content_title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('_page_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('template_key', self.gf('django.db.models.fields.CharField')(default='top_level.html', max_length=255)),
        ))
        db.send_create_signal('page', ['Page'])

        # Adding model 'RichTextContent'
        db.create_table('page_page_richtextcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='richtextcontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['RichTextContent'])

        # Adding model 'MediaFileContent'
        db.create_table('page_page_mediafilecontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mediafile', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(related_name='+', to=orm['medialibrary.MediaFile'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mediafilecontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('type', self.gf('django.db.models.fields.CharField')(default='concertthumbnail', max_length=20)),
        ))
        db.send_create_signal('page', ['MediaFileContent'])

        # Adding model 'FeaturedBoxContent'
        db.create_table('page_page_featuredboxcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='featuredboxcontent_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('series_title', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('series_url', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date_descriptor', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('headliner', self.gf('django.db.models.fields.CharField')(max_length=48, blank=True)),
            ('short_descriptor', self.gf('django.db.models.fields.TextField')()),
            ('poster_thumbnail', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
            ('tickets_url', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('page', ['FeaturedBoxContent'])

        # Adding model 'ImageRotator'
        db.create_table('page_page_imagerotator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imagerotator_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('img', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
        ))
        db.send_create_signal('page', ['ImageRotator'])

        # Adding model 'ImageWrapped'
        db.create_table('page_page_imagewrapped', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imagewrapped_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('img', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
        ))
        db.send_create_signal('page', ['ImageWrapped'])

        # Adding model 'SponsorLogo'
        db.create_table('page_page_sponsorlogo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sponsorlogo_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length='32')),
            ('website_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('img', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile'], null=True, blank=True)),
        ))
        db.send_create_signal('page', ['SponsorLogo'])

        # Adding model 'ConcertDetails'
        db.create_table('page_page_concertdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='concertdetails_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('concert_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('concert_ticket_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('featured_artist_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('featured_artist_role', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('page', ['ConcertDetails'])

        # Adding model 'ConcertArchiveDetails'
        db.create_table('page_page_concertarchivedetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='concertarchivedetails_set', to=orm['page.Page'])),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('page', ['ConcertArchiveDetails'])


    def backwards(self, orm):
        
        # Deleting model 'Page'
        db.delete_table('page_page')

        # Deleting model 'RichTextContent'
        db.delete_table('page_page_richtextcontent')

        # Deleting model 'MediaFileContent'
        db.delete_table('page_page_mediafilecontent')

        # Deleting model 'FeaturedBoxContent'
        db.delete_table('page_page_featuredboxcontent')

        # Deleting model 'ImageRotator'
        db.delete_table('page_page_imagerotator')

        # Deleting model 'ImageWrapped'
        db.delete_table('page_page_imagewrapped')

        # Deleting model 'SponsorLogo'
        db.delete_table('page_page_sponsorlogo')

        # Deleting model 'ConcertDetails'
        db.delete_table('page_page_concertdetails')

        # Deleting model 'ConcertArchiveDetails'
        db.delete_table('page_page_concertarchivedetails')


    models = {
        'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medialibrary.mediafile': {
            'Meta': {'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'page.concertarchivedetails': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ConcertArchiveDetails', 'db_table': "'page_page_concertarchivedetails'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concertarchivedetails_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.concertdetails': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ConcertDetails', 'db_table': "'page_page_concertdetails'"},
            'concert_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'concert_ticket_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'featured_artist_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'featured_artist_role': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concertdetails_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.featuredboxcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'FeaturedBoxContent', 'db_table': "'page_page_featuredboxcontent'"},
            'date_descriptor': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'headliner': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'featuredboxcontent_set'", 'to': "orm['page.Page']"}),
            'poster_thumbnail': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'series_title': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'series_url': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'short_descriptor': ('django.db.models.fields.TextField', [], {}),
            'tickets_url': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'page.imagerotator': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ImageRotator', 'db_table': "'page_page_imagerotator'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imagerotator_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.imagewrapped': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ImageWrapped', 'db_table': "'page_page_imagewrapped'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imagewrapped_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'page.mediafilecontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'MediaFileContent', 'db_table': "'page_page_mediafilecontent'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "'+'", 'to': "orm['medialibrary.MediaFile']"}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'concertthumbnail'", 'max_length': '20'})
        },
        'page.page': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'db_index': 'True', 'blank': 'True'}),
            '_content_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            '_page_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'navigation_extension': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['page.Page']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 17, 14, 55)'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'db_index': 'True'}),
            'template_key': ('django.db.models.fields.CharField', [], {'default': "'top_level.html'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'page.richtextcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'RichTextContent', 'db_table': "'page_page_richtextcontent'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'richtextcontent_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'page.sponsorlogo': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'SponsorLogo', 'db_table': "'page_page_sponsorlogo'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'to': "orm['medialibrary.MediaFile']", 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsorlogo_set'", 'to': "orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'32'"}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['page']
