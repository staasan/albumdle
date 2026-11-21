from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField
    artist = models.CharField
    cover_art = models.CharField
    release_year = models.IntegerField
    genre = models.CharField
