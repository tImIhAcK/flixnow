from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

from .models import Playlist
from flixnow.models import PublishStateOptions

@receiver(pre_save, sender=Playlist)
def publish_playlist_state_pre_save(sender, instance, *args, **kwargs):
    if instance.state == PublishStateOptions.PUBLISH and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif instance.state == PublishStateOptions.DRAFT:
        instance.publish_timestamp = None
            
@receiver(pre_save, sender=Playlist)
def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
            instance.slug = slugify(instance.title)