from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django_filters.filters import RangeFilter

from .forms import CreateUserForm
from .filters import AlbumFilter, SongFilter
from orders.utils import cookieCart, cartData, guestOrder
from orders.models import Order

from .documents import SongDocument
from .models import *

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:        
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'music_store/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
        context = {}
        return render(request, 'music_store/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


# home page
# redirects to login page if not logged in
#@login_required(login_url='login')
def home(request):
    albums = Album.objects.all()
    albumsByPrice = Album.objects.all().order_by('price')
    albumsByPriceReversed = Album.objects.all().order_by('price').reverse()
    albumsByArtist = Album.objects.all().order_by('artist__name')
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    
    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs
    
    context = {'albums':albums, 'genres':genres, 'types':types, 'myFilter':myFilter, 'cartItems':cartItems, 'albumsByPrice':albumsByPrice, 'albumsByPriceReversed':albumsByPriceReversed, 'albumsByArtist':albumsByArtist}
    return render(request, 'music_store/home_page.html', context)

# page with particular album details, comments, songs
#@login_required(login_url='login')
def album(request, pk):
    album = Album.objects.get(id=pk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    songs = album.song_set.all()
    songs = songs.order_by('track_number')

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'album':album, 'genres':genres, 'types':types, 'songs':songs, 'cartItems':cartItems}
    return render(request, 'music_store/album_details.html', context)

# album list by genre
def genre(request, pk):
    genrePk =  Genre.objects.get(id=pk)
    genres =  Genre.objects.all()
    albums = Album.objects.filter(genre=genrePk)
    albumsByPrice = albums.order_by('price')
    albumsByPriceReversed = albums.order_by('price').reverse()
    albumsByArtist = albums.order_by('artist__name')
    types = TypeFormat.objects.all()

    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'albums':albums, 'genres':genres, 'types':types, 'genrePk': genrePk, 'myFilter': myFilter, 'cartItems':cartItems, 'albumsByPrice':albumsByPrice, 'albumsByPriceReversed':albumsByPriceReversed, 'albumsByArtist':albumsByArtist}
    return render(request, 'music_store/album_genre_type.html', context)

# album list by type
def type(request, pk):
    typePk =  TypeFormat.objects.get(id=pk)
    genres =  Genre.objects.all()
    albums = Album.objects.filter(typeFormat=typePk)
    albumsByPrice = albums.order_by('price')
    albumsByPriceReversed = albums.order_by('price').reverse()
    albumsByArtist = albums.order_by('artist__name')
    types = TypeFormat.objects.all()

    myFilter = AlbumFilter(request.GET, queryset=albums)
    albums = myFilter.qs

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'albums':albums, 'genres':genres, 'types':types, 'typePk': typePk, 'myFilter':myFilter, 'cartItems':cartItems,  'albumsByPrice':albumsByPrice, 'albumsByPriceReversed':albumsByPriceReversed, 'albumsByArtist':albumsByArtist}
    return render(request, 'music_store/album_genre_type.html', context)

def albumsList(request):
    return render(request, 'music_store/albums_list.html')

# album list by artist
def songList(request):
    q = request.GET.get('q')
    if q:
        songsq = SongDocument.search().query("multi_match", query=q, type='most_fields', fields=["title", "lyrics", "album.name", "album.artist.name"])
    else:
        songsq = ''
    
    songs2 = Song.objects.all()
    myFilter2 = SongFilter(request.GET, queryset=songs2)
    songs = myFilter2.qs

    data = cartData(request)
    cartItems = data['cartItems']
    
    context = {'songs':songs, 'songsq':songsq, 'myFilter2':myFilter2, 'cartItems':cartItems}
    return render(request, 'music_store/advanced_search.html', context)


# page with artist details, and his albums
def artist(request, pk):
    artist = Artist.objects.get(id=pk)
    genres =  Genre.objects.all()
    types = TypeFormat.objects.all()
    albums = artist.album_set.all()

    data = cartData(request)
    cartItems = data['cartItems']

    context = {'artist':artist, 'genres':genres, 'types':types, 'albums':albums, 'cartItems':cartItems}
    return render(request, 'music_store/artists_page.html', context)
