from django.db import models

# Create your models here.

from django.db import models


class ChatMessage(models.Model):
    text = models.TextField()
    sender = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # 魔术方法”），用于定义对象的字符串表示形式
        return f"{self.sender}: {self.text}"
