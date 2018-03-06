from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url(r'^$',views.index, name='index'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^user/(\d+)', views.user_profile, name='userprofiles'),
    url(r'^search/', views.search_results, name='search_results'),
    url('upload/',views.upload, name='upload'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

