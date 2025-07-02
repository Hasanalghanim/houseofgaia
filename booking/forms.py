from django import forms


class AccessCodeForm(forms.Form):
    code = forms.CharField(label='Enter Access Code', max_length=100)