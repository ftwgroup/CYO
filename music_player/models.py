from django.db import models

class PageSong(models.Model):
    title = models.CharField(max_length=128)