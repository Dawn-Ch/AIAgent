import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
import json

# 从 settings 中获取 DeepSeek API 密钥
DEEPSEEK_API_KEY = settings.DEEPSEEK_API_KEY  # 假设将 API 密钥存储在 settings 中
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # 替换为 DeepSeek 的 API URL

class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get('message', '')

        if not user_message:
            return Response({'reply': '请告诉我你想说什么。'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            headers = {
                "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }

            # 修正请求参数格式
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": user_message}],  # ✅ 使用 messages
                "temperature": 0.7
            }

            response = requests.post(
                DEEPSEEK_API_URL,
                json=payload,
                headers=headers,
                timeout=10
            )

            # 打印调试信息
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)

            response.raise_for_status()  # 检查 HTTP 错误
            response_data = response.json()

            # 修正回复内容提取方式
            bot_reply = response_data.get('choices', [{}])[0].get('message', {}).get('content', '')
            if not bot_reply:
                bot_reply = "未收到有效回复。"

        except requests.exceptions.RequestException as e:
            bot_reply = f"请求失败: {str(e)}"
        except json.JSONDecodeError:
            bot_reply = f"响应解析失败: {response.text[:100]}"  # 截取部分内容避免过长
        except Exception as e:
            bot_reply = f"处理错误: {str(e)}"

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
                     msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')} for msg in messages]
    return JsonResponse({'messages': message_list})
