from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/api/v3/socket/', consumers.SunnyConsumer),
]
