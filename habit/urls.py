from django.urls import path

from habit.apps import AppHabitConfig
from habit.views import HabitCreateAPIView

app_name = AppHabitConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),

]
