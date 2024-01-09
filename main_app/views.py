import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Playlist, Song, User, Photo
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import PlaylistForm


# Create your views here.
def home(request):
    playlists = Playlist.objects.all()
    songs = Song.objects.all()
    return render(request, 'home.html', {
       'playlists': playlists, 
       'songs': songs,
       })

def playlist_index(request):
    playlists = Playlist.objects.all()
    # playlist_fav = user.playlist_set.all()
    return render(request, 'playlists/index.html', {
        'playlists': playlists,
        # 'playlist_fav': playlist_fav
    })

def playlists_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    is_favorite = playlist.user_favorite.filter(id=request.user.id).exists()
    user_favs = playlist.user_favorite.all()
    last_photo = playlist.photo_set.last()
    # create list of songs
    # id_list = playlist.songs.all().values_list('id')
    return render(request, 'playlists/detail.html', {
        'playlist': playlist,
        'playlist_id': int(playlist_id),
        'is_favorite': is_favorite,
        'user_favs' : user_favs,
        'last_photo' : last_photo
    })

# class PlaylistCreate(LoginRequiredMixin, CreateView):
#     model = Playlist
#     fields = ['name', 'description', 'songs']

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         result = super().form_valid(form)
#         # playlist = form.save(commit=False)
#         # playlist.save()
#         print("This is my newly created instance", self.object.pk)
#         return result
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['songs'] = Song.objects.all()
#         context['playlist_form'] = PlaylistForm()
#         return context

# class PlaylistUpdate(LoginRequiredMixin, UpdateView):
#     model = Playlist
#     fields = ['name', 'description', 'songs']

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['songs'] = Song.objects.all()
#         context['playlist_form'] = PlaylistForm()
#         return context

class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    fields = ['name', 'description', 'songs']

    def form_valid(self, form):
        form.instance.user = self.request.user
        result = super().form_valid(form)
        # playlist = form.save(commit=False)
        # playlist.save()
        print("This is my newly created instance", self.object.pk)
        return result
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.all()
        context['playlist_form'] = PlaylistForm()
        return context

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    model = Playlist
    fields = ['name', 'description', 'songs']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Song.objects.all()
        context['playlist_form'] = PlaylistForm()
        return context


class PlaylistDelete(LoginRequiredMixin, DeleteView):
    model = Playlist
    success_url = '/playlists'

class SongList(ListView):
   model = Song

class SongCreate(LoginRequiredMixin, CreateView):
   model = Song
   fields = '__all__'
   success_url = '/songs'
   
class SongDelete(LoginRequiredMixin, DeleteView):
    model = Song
    success_url = '/songs'

# @login_required
# def assoc_song(request, playlist_id, song_id):
#     Playlist.objects.get(id=playlist_id).songs.add(song_id)
#     return redirect('detail', playlist_id=playlist_id)
    
def assoc_song(request, song_id):
    playlists = Playlist.objects.filter(user=request.user)
    
    if request.method == 'POST':
        playlist_id = request.POST.get('playlist')
        if playlist_id:
            playlist = Playlist.objects.get(id=playlist_id)
            song = Song.objects.get(id=song_id)
            playlist.songs.add(song)
            return redirect('detail', playlist_id=playlist_id)

    context = {
        'playlists': playlists,
        'song_id': song_id,
    }

    return render(request, 'associate_song.html', context)

@login_required
def unassoc_song(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).songs.remove(song_id)
  return redirect('detail', playlist_id=playlist_id)

@login_required
def profile_index(request, user_id):
   user = get_object_or_404(User, id=user_id)
   playlists = Playlist.objects.filter(user=user)
   user_favorites = user.playlist_set.all()
   return render(request, 'profile_index.html', {
      'playlists': playlists,
      'profile_user': user,
      'user_favorites': user_favorites
   })

def fav_playlist(request, user_id, playlist_id):
    Playlist.objects.get(id=playlist_id).user_favorite.add(user_id)
    return redirect('detail', playlist_id=playlist_id)

def unfav_playlist(request, user_id, playlist_id):
    Playlist.objects.get(id=playlist_id).user_favorite.remove(user_id)
    return redirect('detail', playlist_id=playlist_id)

def search_view(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(
        Q(name__istartswith=query)
    )
    playlists = Playlist.objects.filter(
        Q(name__icontains=query)
    )
    users = User.objects.filter(
        Q(username__icontains=query)
    )

    return render(request, 'search_bar.html', {
        'songs': songs,
        'playlists': playlists,
        'users': users,
        'query': query  
    })

def songs_search(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(
        Q(name__icontains=query)
    )
    playlists = Playlist.objects.filter(user=request.user)

    context = {
        'query': query,
        'songs': songs,
        'playlists': playlists,
    }

    return render(request, 'main_app/playlist_form.html', context)

def search_bar(request):
    return render(request, 'search_bar.html')

@login_required
def add_photo(request, playlist_id):
    photo_file = request.FILES.get('photo-file', None)
    print(photo_file)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, playlist_id=playlist_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
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
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context) 
