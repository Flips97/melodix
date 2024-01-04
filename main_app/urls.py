from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('playlists/', views.playlist_index, name='index'),
    path('playlists/<int:playlist_id>/', views.playlists_detail, name='detail'),
    path('playlists/create/', views.PlaylistCreate.as_view(), name='playlists_create'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlists_update'),
    path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlists_delete'),
    path('playlists/', views.fav_playlist, name='fav_playlist'),
    path('playlists/<int:playlist_id>/assoc_song/<int:song_id>/', views.assoc_song, name='assoc_song'),
    path('playlists/<int:playlist_id>/unassoc_song/<int:song_id>/', views.unassoc_song, name='unassoc_song'),
    path('songs/', views.SongList.as_view(), name='songs_index'),
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
    path('profile/<int:user_id>/', views.profile_index, name='profile_index'),
    path('search/', views.search_view, name='search_view'),
    path('search_bar/', views.search_bar, name='search_bar_view'),
    path('accounts/signup/', views.signup, name='signup'),
]