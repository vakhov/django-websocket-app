urlpatterns = [
    path('chat/', include('websocket.urls', namespace='websocket')),
]
