from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    service_endpoint = models.URLField(help_text="Push Service Endpoint", unique=True)
    p256dh = models.CharField(max_length=256, help_text="p256 key")
    auth = models.CharField(max_length=256, help_text="Auth key")

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)