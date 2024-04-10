from django.test import TestCase
from .models import Playlist
from flixnow.models import  PublishStateOptions
from django.utils import timezone
from videos.models import Video
from django.utils.text import slugify

# Create your tests here.
class PlaylistModelTestCase(TestCase):
    def setUp(self):
        self.video_a = Video.objects.create(title='This is video title', video_id='abc123')
        self.obj_a = Playlist.objects.create(title='This is the title', video=self.video_a)
        self.obj_b = Playlist.objects.create(title='This is the title 2', state=PublishStateOptions.PUBLISH, video=self.video_a)
        
    def test_video_playlist(self):
        qs = self.video_a.playlist_videos.all()
        self.assertEqual(qs.count(), 2)
        
    def test_valid_title(self):
        title = 'This is the title'
        qs=Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())
        
    def test_created_count(self):
        qs=Playlist.objects.all()
        self.assertGreater(qs.count(), 1)
        
    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)
        
    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISH)
        
        now = timezone.now()
        publish_qs = Playlist.objects.filter(
            publish_timestamp__lte=now,
            state=PublishStateOptions.PUBLISH
        )
        
        self.assertEqual(qs.count(), 1)
        self.assertTrue(publish_qs.exists())
        
        
    def test_publish_manager(self):
        publish_qs = Playlist.objects.published()
        self.assertTrue(publish_qs.exists())
        
        
    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)
        