from django.conf.urls import url, include
from django.contrib import admin
from rateapp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'' , include('rateapp.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]
