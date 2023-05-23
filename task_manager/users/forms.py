from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )


class ChangeForm(UserChangeForm):
    password1 = forms.CharField(label=_("Password"),
                                min_length=3,
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Confirm password"),
                                min_length=3,
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )
