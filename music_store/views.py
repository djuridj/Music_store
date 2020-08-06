from django.shortcuts import render
from django.http import HttpResponse
from .filters import AlbumFilter

# Create your views here.
from .models import *

def home(request):
    albums = Album.objects.all()
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    
    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs
    
    context = {'albums':albums, 'genres':genres, 'types':types,
    'myFilter':myFilter}
    return render(request, 'music_store/home_page.html', context)

def album(request, pk):
    album = Album.objects.get(id=pk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    context = {'album':album, 'genres':genres, 'types':types}
    return render(request, 'music_store/album_details.html', context)

def genre(request, pk):
    genrePk =  Genre.objects.get(id=pk)
    genres =  Genre.objects.all()
    albums = Album.objects.filter(genre=genrePk)
    types = TypeFormat.objects.all()
    context = {'albums':albums, 'genres':genres, 'types':types, 'genrePk': genrePk}
    return render(request, 'music_store/album_genre_type.html', context)

def type(request, pk):
    typePk =  TypeFormat.objects.get(id=pk)
    genres =  Genre.objects.all()
    albums = Album.objects.filter(typeFormat=typePk)
    types = TypeFormat.objects.all()
    context = {'albums':albums, 'genres':genres, 'types':types, 'typePk': typePk}
    return render(request, 'music_store/album_genre_type.html', context)