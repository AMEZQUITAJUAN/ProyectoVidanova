from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Costraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    