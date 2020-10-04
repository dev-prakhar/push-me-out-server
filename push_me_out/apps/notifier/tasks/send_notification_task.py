from apps.notifier.models import NotificationStateManager
from apps.notifier.services.notification_handler_service import NotificationHandlerService
from push_me_out.celery import app


@app.task(bind=True, retry_kwargs={'max_retries': 5})
def send_notification(self, state_manager_id):
    state_manager = NotificationStateManager.objects.filter(pk=state_manager_id).last()
    if state_manager is None:
        return

    state_manager.mark_started()
    try:
        info = NotificationHandlerService(state_manager.subscriber_id).handle()
    except Exception as ex:
        state_manager.mark_failed()
        raise self.retry(exc=ex)
    else:
        state_manager.info = info
        state_manager.mark_completed()