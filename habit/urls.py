from django.urls import path

from app_habit.apps import AppHabitConfig
from app_habit.views import HabitCreateAPIView

app_name = AppHabitConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),

]
