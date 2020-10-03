from rest_framework.generics import CreateAPIView

from apps.notifier.serializers import SubscriberSerializer


class SubscribersView(CreateAPIView):
    serializer_class = SubscriberSerializer
