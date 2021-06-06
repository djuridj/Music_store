from django.urls import path
from music_store import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('album/<str:pk>/', views.album,name="album"),
    #path('album/<str:pk>/', views.albumFromSong,name="albumFromSong"),
    path('genre/<str:pk>/', views.genre,name="genre"),
    path('type/<str:pk>/', views.type,name="type"),
    path('album-list/', views.albumsList,name="albums_list"),
    path('advanced-search/', views.songList,name="song_list"),
    path('artist/<str:pk>/', views.artist, name="artist"),
    #path('artist/<str:pk>/', views.artistFromSong, name="artistFromSong"),
]