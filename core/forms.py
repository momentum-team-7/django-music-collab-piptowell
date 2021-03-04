from django import forms
from .models import Album
from .models import Artist



class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['artist', 'label']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date', 'user', 'photo']