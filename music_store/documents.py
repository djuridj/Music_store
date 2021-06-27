from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Song, Album, Artist

@registry.register_document
class SongDocument(Document):
    
    album = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
        'artist': fields.ObjectField(properties={
            'id': fields.IntegerField(),
            'name': fields.TextField(),
        })
    })
    lyrics = fields.TextField()
    
    class Index:
        name = 'songs'

        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Song
        fields = [
            'id', 'title', 'audio_file',
        ]
        related_models = [Album, Song]
        related_models = [Artist, Album]

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Song):
            return related_instance.Album_set.all()