from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

class User(AbstractUser):
    # Add custom fields if needed
    is_premium = models.BooleanField(default=False)
    mt5_license = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'main'  # Crucial for migrations

    def __str__(self):
        return self.username


class AccountPair(models.Model):
    LIVE = 'LIVE'
    PROP = 'PROP'
    ACCOUNT_TYPES = (
        (LIVE, 'Live Account'),
        (PROP, 'Prop Firm Account'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    account_type = models.CharField(
        max_length=4,
        choices=ACCOUNT_TYPES
    )
    account_number = models.IntegerField()
    password = models.CharField(max_length=255)
    server = models.CharField(max_length=100)
    pair_number = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'account_type', 'pair_number')
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only encrypt on first save
            cipher = Fernet(settings.MT5_ENCRYPTION_KEY)
            self.password = cipher.encrypt(self.password.encode()).decode()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.get_account_type_display()} #{self.account_number}"

class MT5Account(models.Model):
    ACCOUNT_TYPES = (
        ('LIVE', 'Live Account'),
        ('PROP', 'Prop Firm Account'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='user'
    )
    account_type = models.CharField(max_length=4, choices=ACCOUNT_TYPES)
    account_number = models.IntegerField()
    password = models.CharField(max_length=255)  # Encrypted
    server = models.CharField(max_length=100)
    pair_number = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'account_type', 'pair_number')
        verbose_name = 'MT5 Account'
        verbose_name_plural = 'MT5 Accounts'
    
    def save(self, *args, **kwargs):
        # Encrypt password before saving
        if not self.pk or 'password' in kwargs.get('update_fields', []):
            cipher = Fernet(settings.MT5_ENCRYPTION_KEY)
            self.password = cipher.encrypt(self.password.encode()).decode()
        super().save(*args, **kwargs)
    
    def get_password(self):
        cipher = Fernet(settings.MT5_ENCRYPTION_KEY)
        return cipher.decrypt(self.password.encode()).decode()
    
    def __str__(self):
        return f"{self.get_account_type_display()} #{self.account_number} (Pair {self.pair_number})"