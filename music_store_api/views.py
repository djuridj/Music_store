from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer, TypeFormatSerializer, GenreSerializer
from music_store.models import *

# get all albums
@api_view(['GET'])
def albumsView(request):
    albums = Album.objects.all().order_by('-name')
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

# get one album
@api_view(['GET'])
def albumsDetail(request, pk):
    albums = Album.objects.get(id=pk)
    serializer = AlbumSerializer(albums, many=False)
    return Response(serializer.data)

# add new album
@api_view(['POST'])
def albumCreate(request):
	serializer = AlbumSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

# update album
@api_view(['PUT'])
def albumUpdate(request, pk):
	album = Album.objects.get(id=pk)
	serializer = AlbumSerializer(instance=album, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def albumDelete(request, pk):
	album = Album.objects.get(id=pk)
	album.delete()
	return Response('Item succsesfully deleted!')

# get all genres
@api_view(['GET'])
def genresView(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# get all formats
@api_view(['GET'])
def formatsView(request):
    formats = TypeFormat.objects.all()
    serializer = TypeFormatSerializer(formats, many=True)
    return Response(serializer.data)