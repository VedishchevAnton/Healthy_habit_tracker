from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.pagination import MyPagination
from habit.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
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


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyPagination

    def get_queryset(self):
        return Habit.objects.all()


class HabitRetrieveAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
