from django import forms
from .models import Playlist, Song

class PlaylistForm(forms.ModelForm):
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Playlist
        fields = ['name', 'description', 'songs']