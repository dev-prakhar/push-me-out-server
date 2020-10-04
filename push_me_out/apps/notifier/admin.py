from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from apps.notifier.models import Subscriber, NotificationStateManager, NotificationType


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
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return 'subscriber',

        return super().get_readonly_fields(request, obj)


@admin.register(NotificationType)
class NotificationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    fields = ('name', 'options', )
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
