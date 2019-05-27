from django import forms


'''select_choice = [
    ('artist','Artist'),
    ('album','Album'),
    ('track','Track'),
]'''

class searchForm(forms.Form):
    Artist_Info = forms.CharField()
    #Album = forms.CharField()
    #Song = forms.CharField()
    #selected_radio = forms.CharField(label='Make your selection',widget=forms.RadioSelect(choices=select_choice))
