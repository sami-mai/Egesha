from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'lotManager'

urlpatterns = [

    url(r'^$', views.operator, name='operator'),
    url(r'^checkin/$', views.checkin, name='checkin'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
