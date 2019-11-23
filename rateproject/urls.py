from django.conf.urls import url
from django.contrib import admin

from rateapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home/', views.Home.as_view()),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
