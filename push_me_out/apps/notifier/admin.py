from django.contrib import admin

from apps.notifier.models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_endpoint', )
    fields = ('service_endpoint', )
    readonly_fields = ('service_endpoint', )

    def has_add_permission(self, request):
        return False