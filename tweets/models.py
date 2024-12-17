from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",  # Avoid conflict with auth.User.groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",  # Avoid conflict with auth.User.user_permissions
        blank=True,
    )

class Tweet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tweets')
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"
