from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habit.serializers import HabitSerializer


# Create your views here.

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]  # добавляем класс IsAuthenticated для проверки авторизации пользователя

    def perform_create(self, serializer):
        # Получаем авторизированного пользователя
        user = self.request.user
        # Передаем пользователя в качестве значения поля user в создаваемой привычке
        serializer.save(user=user)
