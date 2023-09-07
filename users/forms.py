from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser
from django import forms
from django.core import validators


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(), required=True)
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(), required=True)

    class Meta:
        model = SiteUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
