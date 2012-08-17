from django.template import loader
from django.template.context import Context
from feincms.templatetags.feincms_tags import feincms_render_content
import os
from django.db.models import signals
from django.conf import settings
#from rcs.wiki.models import WikiPage
from feincms.module.page.models import Page
from whoosh.fields import SchemaClass, TEXT, KEYWORD, ID, STORED
from whoosh.index import create_in, open_dir

### Creating the schema
class SiteSchema(SchemaClass):
    path = ID(stored=True)
    title = TEXT(stored=True)
    content = TEXT

### Creating the index
def create_index(sender=None, **kwargs):
    if not os.path.exists("index"):
        os.mkdir("index")
    ix = create_in("index", SiteSchema)

### Render template without request in order to utilize fein template tags to index
def fein_temp_tags(feincms_object):
    t = loader.get_template('search/index.txt')
    c = Context({
        'feincms_object':feincms_object,
    })
    return t.render(c)

ix = open_dir("index") #TODO: (IF) Documentation says "After you've created an
# index, you can open it using the open_dir function"...does that happen here?

#TODO: (IF) this line isn't mentioned in the new version's documentation...
signals.post_syncdb.connect(create_index)

### Adding documents to the index
def update_index(sender, instance, created, **kwargs):
    writer = ix.writer()
    if created:
        writer.add_document(title=instance.title,
                            content=fein_temp_tags(instance),
                            path=unicode(instance.get_absolute_url()))
        writer.commit()
    else:
        writer.update_document(title=instance.title,
                               content=fein_temp_tags(instance),
                               path=unicode(instance.get_absolute_url()))
        writer.commit()

signals.post_save.connect(update_index, sender=Page)
