from django.shortcuts import render

# Create your views here.

# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MessageView(APIView):
    def get(self, request):
        data = {
            'message': 'Hello from Django api!'
        }
        return Response(data, status=status.HTTP_200_OK)

