from django.shortcuts import render


def message_view(request):
    return render(request, 'websocket_message/message.html')
