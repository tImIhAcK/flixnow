from django.contrib import admin
from .models import Video, VideoProxy

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published']
    list_filter = ['active',]
    search_fields = ['title',]
    readonly_fields = ['active', 'is_published', 'publish_timestamp']
    
    
class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title',]
    
    class Meta:
        model = VideoProxy
        
    def get_queryset(self, request):
        return VideoProxy.objects.filter(active=True)
        
admin.site.register(VideoProxy, VideoProxyAdmin)