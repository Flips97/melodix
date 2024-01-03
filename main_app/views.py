from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Playlist, Song

# Create your views here.
def home(request):
    return render(request, 'home.html')

def playlist_index(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/index.html', {
        'playlists': playlists
    })

def playlists_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    # create list of songs
    id_list = playlist.songs.all().values_list('id')
    return render(request, 'playlists/detail.html', {
        'playlist': playlist
    })

class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['songs'] = 'Songs'
       return context
    

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ['name', 'description']

class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = '/playlists'

class SongList(ListView):
   model = Song

class SongCreate(LoginRequiredMixin, CreateView):
   model = Song
   fields = '__all__'
   
class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = 'songs/'

@login_required
def assoc_song(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).songs.add(song_id)
  return redirect('detail', playlist_id=playlist_id)

@login_required
def unassoc_song(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).songs.remove(song_id)
  return redirect('detail', playlist_id=playlist_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Save the user to the db
      user = form.save()
      # Automatically log in the new user
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context) 