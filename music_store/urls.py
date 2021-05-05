from django.urls import path
from music_store import views

urlpatterns = [
    path('', views.home, name="home"),
    path('album/<str:pk>/', views.album,name="album"),
    path('genre/<str:pk>/', views.genre,name="genre"),
    path('type/<str:pk>/', views.type,name="type"),
    path('album-list/', views.albumsList,name="albums_list"),
    path('advanced-search/', views.songList,name="song_list")
]