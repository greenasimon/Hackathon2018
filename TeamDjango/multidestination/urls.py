from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^tripRoad/$', views.trip, name='road'),
 ]
