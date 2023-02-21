from django import forms



class UserReg(forms.form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()
