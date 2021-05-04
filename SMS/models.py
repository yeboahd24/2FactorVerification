from django.db import models
from django.contrib.auth.models import AbstractUser

# Extending the base user
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=1000)