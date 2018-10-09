from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('search/<str:dest>/', views.results, name='results'),

 ]
