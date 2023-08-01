from django.shortcuts import render
from rest_framework import generics

from app_habit.serializers import HabitSerializer


# Create your views here.

class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer



