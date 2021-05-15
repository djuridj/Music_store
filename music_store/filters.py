from django.db.models.fields import DurationField
import django_filters
from django_filters import CharFilter
from django_filters import MultipleChoiceFilter
from django.db.models import Q
from .models import *

# filter for Album search
class AlbumFilter(django_filters.FilterSet):
    
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    artist = CharFilter(field_name='artist__name', lookup_expr='icontains', label='Artist')
    year = CharFilter(field_name='year', lookup_expr='icontains', label='Year')
    class Meta:
        model = Album
        fields = ['name', 'artist', 'year']

# advanced song search
class SongFilter(django_filters.FilterSet):
    feature_artists = CharFilter(field_name='feature_artists__name', lookup_expr='icontains', label='Feature Artists')
    album = CharFilter(field_name='album__name', lookup_expr='icontains', label='Album')
    lyrics = CharFilter(field_name='lyrics', lookup_expr='icontains', label='Lyrics')
    key_words = CharFilter(field_name='key_words__key_word', lookup_expr='icontains', label='Key Words')
    artist = CharFilter(field_name='album__artist__name', lookup_expr='icontains')
    
    class Meta:
        model = Song
        exclude = ['track_number', 'audio_file', 'duration']
        