from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    service_endpoint = models.URLField(help_text="Push Service Endpoint", unique=True)
    p256dh = models.CharField(max_length=256, help_text="p256 key")
    auth = models.CharField(max_length=256, help_text="Auth key")

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class NotificationStateManager(models.Model):
    ENQUEUED = 'enqueued'
    STARTED = 'started'
    COMPLETED = 'completed'
    FAILED = 'failed'
    TASK_STATES = (
        ('enqueued', 'Enqueued'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    )

    subscriber = models.ForeignKey(Subscriber, on_delete=models.DO_NOTHING, null=True, blank=True, help_text="Subscriber to be notified, all subscribers will be notified in case this is null")
    state = models.CharField(max_length=16, choices=TASK_STATES, default=ENQUEUED)

    info = models.JSONField(default=dict, help_text="Helper field to store extra info")

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_enqueued(self):
        self.__set_state(self.ENQUEUED)

    def mark_started(self):
        self.__set_state(self.STARTED)

    def mark_completed(self):
        self.__set_state(self.COMPLETED)

    def mark_failed(self):
        self.__set_state(self.FAILED)

    def __set_state(self, state):
        self.state = state
        self.save()