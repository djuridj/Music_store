from django.db import models
from django.contrib.auth.models import User

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
    year = models.IntegerField()
    record_label = models.CharField(max_length=100)
    album_cover = models.ImageField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    typeFormat = models.ManyToManyField(TypeFormat)
    in_stock = models.IntegerField(default=0, blank=True, null=True)
    avaliable = models.BooleanField(default=True, blank=True, null=True)
    number_of_ratings = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0, blank=True, null=True)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comments = models.CharField(max_length=2000)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    relates_to = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    