from django.urls import path
from . import views

app_name = 'websocket'

urlpatterns = [
    path('', views.get_init_data),
    path('send/', views.send),
]
