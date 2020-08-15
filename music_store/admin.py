from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(TypeFormat)
admin.site.register(Comment)