from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from models import Playlist, Song

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def playlist_index(request):
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'playlists/index.html', {
        'playlists': playlists
    })

@login_required
def playlists_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    # create list of songs

    return render(request, 'playlists/detail.html', {
        'playlist': playlist,
        # needs to render songs
    })

class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['name']

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ['name']

class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = '/playlists'