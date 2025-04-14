from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, AccountPair

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")

class AccountPairForm(forms.ModelForm):
    class Meta:
        model = AccountPair
        fields = [
            'prop_account_login', 
            'prop_account_password',
            'prop_account_server',
            'prop_account_trading_type',
            'live_account_login',
            'live_account_password',
            'live_account_server'
        ]
        widgets = {
            'prop_account_password': forms.PasswordInput(),
            'live_account_password': forms.PasswordInput(),
        }