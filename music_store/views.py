from django.shortcuts import render
from django.http import HttpResponse
from .filters import AlbumFilter, SongFilter
from django.utils.translation import gettext as _

# Create your views here.
from .models import *

#home page
def home(request):
    albums = Album.objects.all()
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    
    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs
    
    context = {'albums':albums, 'genres':genres, 'types':types,
    'myFilter':myFilter}
    return render(request, 'music_store/home_page.html', context)

#page with particular album details, comments, songs
def album(request, pk):
    album = Album.objects.get(id=pk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    songs = album.song_set.all()
    context = {'album':album, 'genres':genres, 'types':types, 
    'songs':songs}
    return render(request, 'music_store/album_details.html', context)

#album list by genre
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

#album list by type
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
