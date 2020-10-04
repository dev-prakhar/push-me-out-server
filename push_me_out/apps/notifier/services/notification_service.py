import logging

from django.conf import settings
from pywebpush import webpush, WebPushException

from apps.notifier.exceptions.push_event_exception import PushEventException

logger = logging.getLogger(__name__)

class NotificationService:
    def __init__(self, subscriber):
        self.subscriber = subscriber

    def trigger_push_event(self, data = None):
        data = data or "Test Notification"
        try:
            webpush(subscription_info=self.__subscription_info(), data=data, vapid_private_key=self.__vapid_private_key(), vapid_claims=self.__vapid_claims())
        except WebPushException as ex:
            logger.error('Push Event Failed for subscriber_id: {subscriber_id} due to error: {err}'.format(subscriber_id=self.subscriber.id, err=repr(ex)))
            # Mozilla returns additional information in the body of the response.
            if ex.response and ex.response.json():
                extra = ex.response.json()
                logger.error("Remote service replied with a {code}:{errno}, {message}".format(code=extra.code, errno=extra.errno, message=extra.message))

            raise PushEventException(str(ex))


    def __subscription_info(self):
        return {
            'endpoint': self.subscriber.service_endpoint,
            'keys': {
                'p256dh': self.subscriber.p256dh,
                'auth': self.subscriber.auth
            }
        }

    def __vapid_private_key(self):
        return settings.APPLICATION_PRIVATE_KEY

    def __vapid_claims(self):
        return {
            'sub': 'mailto:{email}'.format(email=settings.VAPID_EMAIL)
        }
