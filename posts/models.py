from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length = 255, blank = True, null = True)
    content = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    