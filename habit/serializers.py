from rest_framework import serializers

from habit.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    # Поле "user" является внешним ключом к модели User. Запрос к базе данных для получения всех пользователей.
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Habit
        fields = '__all__'
