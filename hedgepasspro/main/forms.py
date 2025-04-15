from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, AccountPair
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # Add custom fields if needed


class AccountPairForm(forms.ModelForm):
    class Meta:
        model = AccountPair
        fields = ['account_type', 'account_number', 'password', 'server', 'pair_number']
        widgets = {
            'password': forms.PasswordInput(),
        }
