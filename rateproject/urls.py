from django.conf.urls import url, include
from django.contrib import admin

from rateapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
