from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from flixnow.models import PublishStateOptions
from videos.models import Video

class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(
            publish_timestamp__lte=now,
            state=PublishStateOptions.PUBLISH
        )
        
class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()


class Playlist(models.Model):
    video = models.ForeignKey(Video, related_name='playlist_videos', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
    objects = PlaylistManager()
    
    @property
    def is_published(self):
        return self.active
    
