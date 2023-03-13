from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from profiles.models import ProfileCategory

COLOR_PALETTE = [
    ("#C70039", "red"),
    ("#0096FF", "blue"),
    ("#FFFFFF", "white"),
    ("#848484", "gray"),
    ("#6A00DF", "purple"),
    ("#00A131", "green"),
    ("#FFC300", "yellow"),
]


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ListCreateForm(forms.ModelForm):
    class Meta:
        model = ProfileCategory
        fields = ('name', 'color')
