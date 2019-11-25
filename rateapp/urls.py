from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   url('^$', views.landing,name='landing'),
   url('^home/$', views.home, name='home'),
   url(r'^upload/$', views.create_post, name='create_post'),
   url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
   url(r'^search/$', views.search, name='search_results'),
     
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)