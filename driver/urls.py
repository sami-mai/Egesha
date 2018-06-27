from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'driver'

urlpatterns = [
    url(r'^search/', views.search_location, name='Search'),
    url(r'^edit-profile/', views.edit_profile, name='edit_profile'),
    url(r'^car-details/', views.car_details, name='car_details'),
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.homed, name='homed'),
    url(r'^pay/$', views.trigger_payment, name='trigger_payment'),
    url(r'^status-success/$', views.status_success, name='status_success'),
    url(r'^status-failed/$', views.status_failed, name='status_failed'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
