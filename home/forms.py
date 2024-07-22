from django import forms


class SearchHomeForm(forms.Form):

    query = forms.CharField(max_length=100, label="search")