import django_filters
from django_filters import CharFilter
from .models import *

class AlbumFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains',label='')
    class Meta:
        model = Album
        fields = ['name']