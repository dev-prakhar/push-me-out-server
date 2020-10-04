from django.contrib import admin

from apps.notifier.models import Subscriber, NotificationStateManager


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_endpoint', )
    fields = ('service_endpoint', )
    readonly_fields = ('service_endpoint', )

    def has_add_permission(self, request):
        return False

@admin.register(NotificationStateManager)
class NotificationStateManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscriber_id', 'state',)
    fields = ('subscriber', 'state', 'info')
    readonly_fields = ('info', )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('subscriber', )

        return super().get_readonly_fields(request, obj)