from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
import json


class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get('message', '')

        # 处理用户消息，这里只是一个简单的示例
        if user_message:
            bot_reply = f"你刚刚说: {user_message}, 我会在稍后提醒你！"
        else:
            bot_reply = "请告诉我你想说什么。"

        # 返回机器人的回复
        return Response({'reply': bot_reply}, status=status.HTTP_200_OK)


@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('text')
        sender = data.get('sender')

        if text and sender:
            # 保存到数据库
            ChatMessage.objects.create(text=text, sender=sender)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing text or sender'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


def get_messages(request):
    messages = ChatMessage.objects.all().order_by('timestamp')
    message_list = [{'text': msg.text, 'sender': msg.sender, 'timestamp':
                     msg.timestamp.strftime('%Y-%m-%d %H: %M:%S')} for msg in messages]
    return JsonResponse({'messages': message_list})