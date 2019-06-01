from django.contrib import admin

from .models import Song, Album, Artists


admin.site.register(Artists)
admin.site.register(Album)
admin.site.register(Song)
