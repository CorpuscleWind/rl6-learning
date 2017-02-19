from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/300/', admin.site.urls),
    url(r'^', include('core.urls', 'core')),
    url(r'^discipline/', include('learning.urls', 'learning')),
    url(r'^feedback/', include('feedback.urls', 'feedback'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
