from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'lotOwner'

urlpatterns=[
    url(r'^owner/',views.home, name='Lot'),
    url(r'^details/(\d+)',views.Lotdetail,name='Details'),
    url(r'^map/(\d+)',views.map,name='Map'),
    url(r'^location/(\d+)',views.location,name='Location'),
    url(r'^edit/(\d+)',views.edit_profile,name='Edit'),
    url(r'^edit_lot/(\d+)',views.edit_lot,name='Edit_Lot'),
    url(r'^payment/(\d+)',views.payment,name="Payment"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
