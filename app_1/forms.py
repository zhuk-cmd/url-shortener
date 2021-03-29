from django import forms

class URLForms(forms.Form):
    url = forms.CharField(label='URL')