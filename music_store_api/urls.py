from django.urls import path
from music_store_api import views

urlpatterns = [
    path('albums/', views.albumsView, name="albums_list"),
    path('albums/<str:pk>', views.albumsDetail, name="album_get"),
    path('album-create', views.albumCreate, name="album_create"),
    path('album-update/<str:pk>', views.albumUpdate, name="album_update"),
    path('album-delete/<str:pk>', views.albumDelete, name="album_delete"),
    path('genres/', views.genresView, name="genres_list"),
    path('formats/', views.formatsView, name="formats_list"),
]
