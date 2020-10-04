from django.db import transaction

from apps.notifier.models import NotificationStateManager
from apps.notifier.tasks.send_notification_task import send_notification


class NotificationStateManagerService:
    def __init__(self, data):
        self.data = data

    def insert(self):
        subscriber_id = self.data.get('subscriber_id')
        with transaction.atomic():
            state_manager = NotificationStateManager.objects.create(subscriber_id=subscriber_id)
            transaction.on_commit(lambda: send_notification.delay(state_manager.id))

        return state_manager