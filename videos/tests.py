from django.test import TestCase
from .models import Video
# Create your tests here.
class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='This is the title')
        
    def test_valid_title(self):
        title = 'This is the title'
        qs=Video.objects.filter(title=title)
        self.assertTrue(qs.exists())
        
    def test_created_count(self):
        qs=Video.objects.all()
        self.assertEqual(len(qs), 1)