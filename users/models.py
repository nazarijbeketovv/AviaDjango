from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users/avatars/%Y/%m/%d", blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)


    def get_tickets_list(self):
        return list(self.tickets.all())
