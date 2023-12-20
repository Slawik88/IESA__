# eventsApp/urls.py
from django.urls import path
from .views import event_list, register_for_event

app_name = 'eventsApp'

urlpatterns = [
    path('events/', event_list, name='event_list'),
    path('events/<int:event_id>/register/', register_for_event, name='register_for_event'),

]
