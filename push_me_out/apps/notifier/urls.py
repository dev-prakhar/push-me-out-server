from django.urls import path

from apps.notifier import views

urlpatterns = [
    path('subscribers/', views.SubscribersView.as_view(), name='subscribers_view'),
    path('trigger/', views.TriggerNotification.as_view(), name='trigger_notification_view'),
    path('notification_types/', views.NotificationTypesView.as_view(), name='notification_types_view'),
]
