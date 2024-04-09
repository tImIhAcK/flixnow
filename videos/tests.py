from django.test import TestCase
from .models import Video
from django.utils import timezone
from django.utils.text import slugify

# Create your tests here.
class VideoModelTestCase(TestCase):
    def setUp(self):
        self.obj_a = Video.objects.create(title='This is the title', video_id='askdjk')
        self.obj_b = Video.objects.create(title='This is the title 2', state=Video.VideoStateOptions.PUBLISH, video_id='laksldkalsd')
        
    def test_valid_title(self):
        title = 'This is the title'
        qs=Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
        
    def test_created_count(self):
        qs=Video.objects.all()
        self.assertGreater(qs.count(), 1)
        
    def test_draft_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)
        
    def test_publish_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.PUBLISH)
        
        now = timezone.now()
        publish_qs = Video.objects.filter(
            publish_timestamp__lte=now,
            state=Video.VideoStateOptions.PUBLISH
        )
        
        self.assertEqual(qs.count(), 1)
        self.assertTrue(publish_qs.exists())
        
        
    def test_publish_manager(self):
        publish_qs = Video.objects.published()
        self.assertTrue(publish_qs.exists())
        
        
    def test_slug_field(self):
        title = self.obj_a.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_a.slug)
        