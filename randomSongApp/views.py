from django.shortcuts import render
from randomSongApp.forms import searchForm

# Create your views here.

def index(request):
    return render(request,'randomSongApp/home.html')

def searchFormView(request):
    form = searchForm()
    return render(request,'randomSongApp/searchpage.html',{'form':form})
