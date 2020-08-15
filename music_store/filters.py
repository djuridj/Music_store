import django_filters
from django_filters import CharFilter
from django.db.models import Q
from .models import *

class AlbumFilter(django_filters.FilterSet):
    
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name:')
    artist = CharFilter(field_name='artist', lookup_expr='icontains', label='Artist:')
    year = CharFilter(field_name='year', lookup_expr='icontains', label='Year:')
    class Meta:
        model = Album
        fields = ['name', 'artist', 'year']