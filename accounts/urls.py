from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [

    url(r'^accounts/', include('registration.backends.simple.urls', namespace='auth')),
    url(r'^account/', include('social_django.urls', namespace='social')),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {"next_page": '/'}),
    url(r'^account/(?P<username>[-\w]+)/$', account_views.edit_profile, name='edit_profile'),
    # url(r'^dashboard/(?P<username>[-\w]+)/$', account_views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
