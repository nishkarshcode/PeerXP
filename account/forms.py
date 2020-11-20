from django import forms

# Code from here

class LoginForm(forms.Form):
    email               = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    password            = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))