from django.db.models.fields import DurationField
import django_filters
from django_filters import CharFilter
from django_filters import MultipleChoiceFilter
from django.db.models import Q
from django_filters.filters import ChoiceFilter
from .models import *

# filter for Album search
class AlbumFilter(django_filters.FilterSet):
    q = CharFilter(method='custom_filter', label='Search')

    class Meta:
        model = Album
        fields = ['q']

    def custom_filter(self, queryset, name, value):
        return Album.objects.filter(Q(name__icontains=value) | Q(artist__name__icontains=value) | Q(year__icontains=value) | Q(record_label__icontains=value))
        

# advanced song search
class SongFilter(django_filters.FilterSet):
    feature_artists = CharFilter(field_name='feature_artists__name', lookup_expr='icontains', label='Feature Artists')
    album = CharFilter(field_name='album__name', lookup_expr='icontains', label='Album')
    lyrics = CharFilter(field_name='lyrics', lookup_expr='icontains', label='Lyrics')
    key_words = CharFilter(field_name='key_words__key_word', lookup_expr='icontains', label='Key Words')
    artist = CharFilter(field_name='album__artist__name', lookup_expr='icontains')
    
    class Meta:
        model = Song
        exclude = ['track_number', 'audio_file']
        