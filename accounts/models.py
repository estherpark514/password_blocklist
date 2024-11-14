from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from cryptography.fernet import Fernet, InvalidToken
from django.conf import settings

cipher_suite = Fernet(settings.SECRET_ENCRYPTION_KEY)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    encrypted_password = models.BinaryField()
    raw_password = models.CharField(max_length=128, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def set_password(self, raw_password):
        """Encrypt and set the password, and save the raw password for research."""
        encrypted_password = cipher_suite.encrypt(raw_password.encode())
        self.encrypted_password = encrypted_password
        
        self.raw_password = raw_password

    def check_password(self, raw_password):
        """Check the raw password by decrypting the stored password."""
        try:
            decrypted_password = cipher_suite.decrypt(self.encrypted_password).decode()
            return decrypted_password == raw_password
        except InvalidToken:
            print("Decryption failed: Invalid token. Check your encryption key.")
            print(f"Encrypted password: {self.encrypted_password}")
            print(f"Encryption key used: {settings.SECRET_ENCRYPTION_KEY}")
            return False

    def __str__(self):
        return self.email
