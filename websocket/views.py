from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_init_data(request):
    return render(request, 'websocket/init_data.html')


def parse_message(request, message_default='Hello'):
    message = str()
    if request.method == 'GET':
        message = request.GET.get('message', message_default)
    if request.method == 'POST':
        message = request.POST.get('message', message_default)

    return 'PONG' if 'ping' in message.lower() else message


@api_view(['GET', 'POST'])
def send(request):
    """
    Метод проверки отправки socket сообщений.

    Метод проверки отправки socket сообщений. Обрабатывает GET и POST запрос. Без передачи параметров, возврает Hello.
    При передаче параметра message с непустым знгачением, возвращает это значение. Отвечает на ping

    Example:<br>
        request - http://localhost:8000/api/v3/chat/send/<br>
        response wss - Hello<br>
        request - http://localhost:8000/api/v3/chat/send/?message=123<br>
        response wss - 123<br>
    """
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('chat_sunny', {
        'type': 'chat_message',
        'message': parse_message(request)
    })
    return Response('Done')
