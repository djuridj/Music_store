from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer
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