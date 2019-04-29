from django.shortcuts import render
from randomSongApp.forms import searchForm
import requests




def index(request):
    return render(request,'randomSongApp/home.html')

def searchFormView(request):
    form = searchForm()
    if request.method == "POST":
        url = 'https://accounts.spotify.com/api/token'
        payload = {'client_id': '2f9fe9c1bb0f44fbaa27e0b1addc958d' ,'client_secret': 'dba5b3924f5f4ee2a6b582a0a70ad270'}
        headers = {
            'Authorization': 'Basic {{client_credentials}}'
        }
        r = requests.post(url, headers = headers, data=payload)
        print(r.text)
    #return render(request,'randomSongApp/searchpage.html',{'form':form})
