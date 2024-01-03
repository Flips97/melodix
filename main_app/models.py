from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('songs_detail', kwargs={'pk': self.id})

class Playlist(models.Model):
    name =  models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, blank=True)
    user_favorite = models.ManyToManyField(User, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_playlist_set')
    description = models.TextField(max_length=250)
