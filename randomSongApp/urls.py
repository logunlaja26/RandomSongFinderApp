from django.conf.urls import url
from django.urls import path
from randomSongApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('/searchpage',views.searchFormView,name='searchForm'),
    path('/searchpage',views.getArtist,name='searchForm'),
]
