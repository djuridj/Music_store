from django.shortcuts import render
from django.http import HttpResponse
from .filters import AlbumFilter, SongFilter
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from .models import *

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'music_store/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'music_store/login.html', context)


# home page
def home(request):
    albums = Album.objects.all()
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    
    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs
    
    context = {'albums':albums, 'genres':genres, 'types':types,
    'myFilter':myFilter}
    return render(request, 'music_store/home_page.html', context)

# page with particular album details, comments, songs
def album(request, pk):
    album = Album.objects.get(id=pk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    songs = album.song_set.all()
    context = {'album':album, 'genres':genres, 'types':types, 
    'songs':songs}
    return render(request, 'music_store/album_details.html', context)

# album list by genre
def genre(request, pk):
    genrePk =  Genre.objects.get(id=pk)
    genres =  Genre.objects.all()
    albums = Album.objects.filter(genre=genrePk)
    types = TypeFormat.objects.all()
    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs
    context = {'albums':albums, 'genres':genres, 'types':types, 
    'genrePk': genrePk, 'myFilter': myFilter}
    return render(request, 'music_store/album_genre_type.html', context)

# album list by type
def type(request, pk):
    typePk =  TypeFormat.objects.get(id=pk)
    genres =  Genre.objects.all()
    albums = Album.objects.filter(typeFormat=typePk)
    types = TypeFormat.objects.all()
    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs
    context = {'albums':albums, 'genres':genres, 'types':types, 
    'typePk': typePk, 'myFilter':myFilter}
    return render(request, 'music_store/album_genre_type.html', context)

def albumsList(request):
    return render(request, 'music_store/albums_list.html')

# album list by artist
def songList(request):
    songs = Song.objects.all()
    myFilter2 = SongFilter(request.GET, queryset=songs)
    songs = myFilter2.qs
    context = {'songs':songs, 'myFilter2':myFilter2}
    return render(request, 'music_store/advanced_search.html', context)

# page with particular album details, songs
def albumFromSong(request, pk):
    songPk = Song.objects.get(id=pk)
    album = Album.objects.filter(song=songPk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    songs = album.song_set.all()
    context = {'songPk':songPk, 'album':album, 'genres':genres, 'types':types, 
    'songs':songs}
    return render(request, 'music_store/album_details.html', context)

# page with album details, and his albums
def artistFromAlbum(request, pk):
    artist = Artist.objects.get(id=pk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    albums = artist.album_set.all()
    context = {'artist':artist, 'genres':genres, 'types':types, 
    'albums':albums}
    return render(request, 'music_store/artists_page.html', context)