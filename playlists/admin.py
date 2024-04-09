from django.contrib import admin
from .models import Playlist

# Register your models here.
@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'slug']
    list_filter = ['active',]
    search_fields = ['title',]
    readonly_fields = ['active', 'is_published', 'publish_timestamp']
    