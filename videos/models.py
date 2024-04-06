from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    class VideoStateOptions(models.TextChoices):
        PUBLISH = 'PU', 'Publish'
        DRAFT = 'DR', 'Draft'
        # UNLISTED = 'UN', 'Unlisted'
        # PRIVATE = 'PR', 'Private'
    
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500, blank=True, null=True)
    video_id = models.CharField(max_length=60)  # Youtube Video ID
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)
    state = models.CharField(max_length=2, choices=VideoStateOptions.choices, default=VideoStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
    @property
    def is_published(self):
        return self.active
    
    def save(self, *args, **kwargs):
        if self.state == self.VideoStateOptions.PUBLISH and self.publish_timestamp is None:
            print('save as timestamp for published')
            self.publish_timestamp = timezone.now()
        elif self.state == self.VideoStateOptions.DRAFT:
            self.publish_timestamp = None
        super().save(*args, **kwargs)
            

class VideoProxy(Video):
    class Meta:
        proxy = True
        verbose_name = 'published video'
        verbose_name_plural = 'published videos'
    
    
