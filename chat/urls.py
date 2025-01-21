from django.urls import path
from .views import ChatView, save_message, get_messages

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('chat/save/', save_message, name='save_message'),  # 修改为 /api/chat/save/
    path('chat/history/', get_messages, name='get_messages'),  # 修改为 /api/chat/history/
]
