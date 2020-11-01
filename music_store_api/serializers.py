from rest_framework import serializers
from music_store.models import Album, TypeFormat, Genre

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class TypeFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeFormat
        fields = '__all__'