from django.form import ModelForm
from .models import Playlist, Song

class PlaylistForm(ModelForm):
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Playlist
        fields = ['name', 'description', 'songs']