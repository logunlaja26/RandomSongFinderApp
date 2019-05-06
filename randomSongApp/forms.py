from django import forms


class searchForm(forms.Form):
    Artist = forms.CharField()
    #Album = forms.CharField()
    #Song = forms.CharField()
