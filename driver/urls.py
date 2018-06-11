from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^profileform/',views.profileform,name = 'profileform'),
url(r'^cardetails/',views.cardetails,name = 'cardetails'),
url(r'^$',views.index,name ='index'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
