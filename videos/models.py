from django.db import models
from django.utils import timezone
from django.utils.text import slugify

    
class VideoQuerySet(models.QuerySet):
    now = timezone.now()
    def published(self):
        now = timezone.now()
        return self.filter(
            publish_timestamp__lte=now,
            state=Video.VideoStateOptions.PUBLISH
        )
        
class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()


class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN', 'Unlisted'
        # PRIVATE = 'PR', 'Private'
    
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500, blank=True, null=True)
    video_id = models.CharField(max_length=60, unique=True)  # Youtube Video ID
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
    objects = VideoManager()
    
    @property
    def is_published(self):
        return self.active
    
    def save(self, *args, **kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.publish_timestamp is None:
            print('save as timestamp for published')
            self.publish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.publish_timestamp = None
            
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
            

class VideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'published video'
        verbose_name_plural = 'published videos'
    
    
