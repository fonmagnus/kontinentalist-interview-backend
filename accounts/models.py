from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, role, is_staff=False, is_superuser=False, password=None):
        if not name:
            raise ValueError('User must have name')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            role=role,
            password=password,
            is_staff=(role == 'Admin'),
            is_superuser=(role == 'Admin')
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, role='Admin', is_staff=True, is_superuser=True, password=None):
        user = self.create_user(
            email=email,
            name=name,
            role=role,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'Admin'
        MEMBER = 'Member'

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=15, choices=Role.choices, default='Member')
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    def __str__(self):
        return self.name
