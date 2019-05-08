from django.conf.urls import url
from django.urls import path
from randomSongApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('/search',views.searchFormView,name='searchForm'),
    path('/search/artist',views.getArtist,name='searchForm'),
]
