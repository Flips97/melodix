from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('songs_index', kwargs={'pk': self.id})

class Playlist(models.Model):
    name =  models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, blank=True)
    user_favorite = models.ManyToManyField(User, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_playlist_set')
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'playlist_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for playlist_id: {self.playlist_id} @{self.url}", f"Photo for user_id: {self.user_id} @{self.url}"
    
    
