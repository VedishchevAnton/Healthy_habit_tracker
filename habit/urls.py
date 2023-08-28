from django.urls import path

from habit.apps import AppHabitConfig
from habit.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitDestroyAPIView, \
    HabitUpdateAPIView

app_name = AppHabitConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete')

]
