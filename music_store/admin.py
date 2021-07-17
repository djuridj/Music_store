from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(TypeFormat)
admin.site.register(Mood)
admin.site.register(KeyWords)
admin.site.register(Vocal)
admin.site.register(NotableInstrument)
admin.site.register(Song)
