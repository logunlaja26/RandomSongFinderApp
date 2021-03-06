from django.shortcuts import render
from randomSongApp.forms import searchForm
from pprint import pprint
import requests



def index(request):
    return render(request,'randomSongApp/home.html')

def searchFormView(request):
    form = searchForm()
    if request.method == "POST":
        url = 'https://accounts.spotify.com/api/token'
        payload = {'grant_type':'client_credentials','client_id': '2f9fe9c1bb0f44fbaa27e0b1addc958d' ,'client_secret': 'dba5b3924f5f4ee2a6b582a0a70ad270'}
        r = requests.post(url, data=payload)
    return render(request,'randomSongApp/searchpage.html',{'form':form})

def getArtist(request):
    print("get artist was called")
    if request.method == "POST":
        auth_url = 'https://accounts.spotify.com/api/token'
        payload = {'grant_type':'client_credentials','client_id': '2f9fe9c1bb0f44fbaa27e0b1addc958d' ,'client_secret': 'dba5b3924f5f4ee2a6b582a0a70ad270'}
        r = requests.post(auth_url, data=payload)
        access_token = (r.json())['access_token']

        form = searchForm(request.POST)
        if not form.is_valid():
            return render(request,'randomSongApp/searchpage.html',{'form': searchForm()})
        url_safe_artist = request.POST["Artist"]
        url = f'https://api.spotify.com/v1/search?q={url_safe_artist}&type=artist'
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer %s' %access_token
        }
        #print('-- Headers %s ---' %headers)
        response = requests.get(url, headers=headers)
        results = (response.json()["artists"]["items"])
        context  = {
            'artist_name': (results[0]["name"]),
            'artist_followers': (results[0]["followers"]["total"]),
            'artist_popularity': (results[0]["popularity"])
        }

        #pprint(results)
        #print(type(results))
    return render(request,'randomSongApp/searchpage.html',{'form':searchForm(),'context':context})

    def getAlbum(request):
        if request.method == "POST":
            auth_url = 'https://accounts.spotify.com/api/token'
            payload = {'grant_type':'client_credentials','client_id': '2f9fe9c1bb0f44fbaa27e0b1addc958d' ,'client_secret': 'dba5b3924f5f4ee2a6b582a0a70ad270'}
            r = requests.post(auth_url, data=payload)
            access_token = (r.json())['access_token']

            form = searchForm(request.POST)
            if not form.is_valid():
                return render(request,'randomSongApp/searchpage.html',{'form': searchForm()})

            url = 'https://api.spotify.com/v1/search?q=The+Massacre&type=artist'
            headers = {
                'Accept': 'application/json',
                'Authorization': 'Bearer %s' %access_token
            }
            print('-- Headers %s--'%headers)
