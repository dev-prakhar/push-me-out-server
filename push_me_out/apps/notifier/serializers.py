from rest_framework import serializers

from apps.notifier.models import Subscriber, NotificationType


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id', 'service_endpoint', 'p256dh', 'auth')
        extra_kwargs = {
            'p256dh': {'write_only': True},
            'auth': {'write_only': True},
        }


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ('id', 'name', )