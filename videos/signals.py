from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify

from .models import Video, PublishStateOptions

@receiver(pre_save, sender=Video)
def publish_video_state_pre_save(sender, instance, *args, **kwargs):
    if instance.state == PublishStateOptions.PUBLISH and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
    elif instance.state == PublishStateOptions.DRAFT:
        instance.publish_timestamp = None
            
@receiver(pre_save, sender=Video)
def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
            instance.slug = slugify(instance.title)