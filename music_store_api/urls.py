from django.urls import path
from music_store_api import views

urlpatterns = [
    path('albums/', views.albumsView, name="albums_api"),
    path('albums/<str:pk>', views.albumsDetail, name="album_api"),
]
