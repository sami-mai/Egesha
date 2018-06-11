from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^owner/(\d+)', views.home, name='Lot'),
    # url(r'^details/(\d+)', views.Lotdetail, name='Details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
