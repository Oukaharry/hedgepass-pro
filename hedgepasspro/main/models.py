from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django_cryptography.fields import encrypt
from main.utils.baseconv import BaseConverter  

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True)
    two_factor_enabled = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

class AccountPair(models.Model):
    TRADING_TYPES = [('manual', 'Manual'), ('algo', 'Algorithmic')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_pairs')
    prop_account_login = models.CharField(max_length=100)
    prop_account_password = encrypt(models.CharField(max_length=100))
    prop_account_server = models.CharField(max_length=100)
    prop_account_trading_type = models.CharField(max_length=10, choices=TRADING_TYPES)
    live_account_login = models.CharField(max_length=100)
    live_account_password = encrypt(models.CharField(max_length=100))
    live_account_server = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Pair {self.id} - {self.prop_account_login}"

class PerformanceData(models.Model):
    pair = models.ForeignKey(AccountPair, on_delete=models.CASCADE, related_name='performance_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    live_equity = models.DecimalField(max_digits=12, decimal_places=2)
    hedge_equity = models.DecimalField(max_digits=12, decimal_places=2)
    efficiency = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-timestamp']