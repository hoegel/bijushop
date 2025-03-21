from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birthday_date = models.DateField(default="2000-01-01")