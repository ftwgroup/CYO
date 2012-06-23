import os
from django.db.models import signals
from django.conf import settings
from rcs.wiki.models import WikiPage
from whoosh import index, store, fields

WHOOSH_SCHEMA = fields.Schema(title=fields.TEXT(stored=True),
                              content=fields.TEXT,
                              url=fields.ID(stored=True, unique=True))

def create_index(sender=None, **kwargs):
    if not os.path.exists(settings.WHOOSH_INDEX):
        os.mkdir(settings.WHOOSH_INDEX)
        storage = store.FileStorage(settings.WHOOSH_INDEX)
        ix = index.Index(storage, schema=WHOOSH_SCHEMA, create=True)

signals.post_syncdb.connect(create_index)

def update_index(sender, instance, created, **kwargs):
    storage = store.FileStorage(settings.WHOOSH_INDEX)
    ix = index.Index(storage, schema=WHOOSH_SCHEMA)
    writer = ix.writer()
    if created:
        writer.add_document(title=unicode(instance, content=instance.content,
                            url=unicode(instance.get_absolute_url()))
        writer.commit()
    else:
        writer.update_document(title=unicode(instance), content=instance.content,
                               url=unicode(instance.get_absolute_url()))
        writer.commit()

signals.post_save.connect(update_index, sender=WikiPage)

