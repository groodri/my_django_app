from django import forms
from hello.models import *

class registerForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'name',
            'surnames',
            'signature',
            'degree',
            'university',
            'cv',
            'email',
            'password',
            ]
        
        widgets = {
            'password': forms.PasswordInput(),
        }

class loginForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'email',
            'password',
        ]

        widgets = {
            'password': forms.PasswordInput(),
        }