from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist_detail.html', {'artist': artist})