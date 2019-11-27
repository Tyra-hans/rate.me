from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from rateapp.views import UserViewSet, ProfileViewSet,ProjectViewSet
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'' , include('rateapp.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'api-token-auth/', obtain_auth_token)
]
