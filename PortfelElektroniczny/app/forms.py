"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Login'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Haslo'}))
    

class Rejestracja(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        label="Nazwa użytkownika",
        widget=forms.TextInput(
            attrs={
                "class": "example-html-class",
                "placeholder": "Nazwa użytkownika"
            }
        )
    )  # It's a example extend field. You can do it for all field .
 
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]