from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=64, default='generic_album')
    artist = models.CharField(max_length=64, default='generic_artist')
    cover_art = models.CharField(max_length=64, default='generic_cover')
    release_year = models.IntegerField(default=1970)
    genre = models.CharField(max_length=64, default='generic_genre')
