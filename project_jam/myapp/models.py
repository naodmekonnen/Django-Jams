from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=225)
    def __str__ (self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=225)
    def __str__ (self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=225)
    def __str__ (self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=225)
    def __str__ (self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=225)
    duration = models. DecimalField(max_digits = 3, decimal_places = 2, null=False)
    plays = models.IntegerField(default=0)
    # artist_id = models.ForeignKey(Artist, on_delete=models.PROTECT, null=True)
    # album_id = models.ForeignKey(Album, on_delete=models.PROTECT,null=True)
    genre_id = models.ForeignKey(Genre, on_delete=models.PROTECT,null=True)
    artist = models.ManyToManyField(Artist)
    album = models.ManyToManyField(Album)
    playlist = models.ManyToManyField(Playlist)
    def __str__ (self):
        return self.title




