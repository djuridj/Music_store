from django.db import models

# Create your models here.

class Genre(models.Model):
    GENRE = (
        ('Rock', 'Rock'),
        ('HipHop', 'HipHop'),
        ('Electronic', 'Electronic'),
    )
    genre = models.CharField(max_length=50, null=True, choices=GENRE)

    def __str__(self):
        return self.genre

class TypeFormat(models.Model):
    TYPE = (
        ('Vinyl', 'Vinyl'),
        ('CD', 'CD'),
        ('Cassette', 'Cassette'),
    )
    types = models.CharField(max_length=50, null=True, choices=TYPE)

    def __str__(self):
        return self.types

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField(max_length=4)
    record_label = models.CharField(max_length=100)
    album_cover = models.ImageField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    typeFormat = models.ManyToManyField(TypeFormat)

    def __str__(self):
        return self.name

