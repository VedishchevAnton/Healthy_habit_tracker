from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User
from django.urls import reverse


# Create your tests here.

class HabitTestCase(APITestCase):

    def setUp(self):
        # Создание тестового пользователя
        self.user = User.objects.create_user(
            email='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)

        # Создание тестовой привычки
        self.habit = Habit.objects.create(
            user=self.user,
            place='Квартира',
            time="10:00:00",
            action='Медитация',
            pleasant=True,
            period=1,
            time_to_complete=10
        )

    def test_create_habit(self):
        """
        Тест для создания привычек
        """
        url = reverse('habit:habit-create')
        data = {
            'user': self.user.id,
            'place': 'Дом',
            'time': '08:00:00',
            'action': 'Игра в World of Warcraft',
            'pleasant': False,
            'period': 8,
            'time_to_complete': 15
        }

        response = self.client.post(url, data, format='json')  # Отправка POST-запроса для создания привычки

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)  # Проверка, что код статуса ответа равен 201 (Создан)
        self.assertEqual(Habit.objects.count(), 2)  # Проверка, что был создан объект пивычки

    def test_list_habits(self):
        """
        Тест для получения списка привычек
        """
        url = reverse('habit:habit-list')  # Получение URL для получения списка привычек
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя
        response = self.client.get(url)  # Отправка GET-запроса на получение списка привычек
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа (должен быть 200 OK)
        self.assertEqual(len(response.data), 4)  # Проверка количества привычек в ответе (должно быть 4)

    def test_retrieve_habit(self):
        """
        Тест для получения информации о конкретной привычке
        """
        url = reverse('habit:habit-get', args=[self.habit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Квартира')  # Проверка места привычки

    def test_update_habit(self):
        """
        Тест для обновления информации о привычке
        """
        url = reverse('habit:habit-update',
                      args=[self.habit.id])  # Получаем URL для обновления привычки с определенным идентификатором
        data = {'place': 'Офис'}  # Задаем новое значение для поля "place"
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)  # Отправляем PATCH-запрос на указанный URL с новыми данными
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'],
                         'Офис')  # Проверяем, что значение поля "place" в ответе соответствует заданному значению

    def test_destroy_habit(self):
        """
        Тест для удаления привычки
        """
        url = reverse('habit:habit-delete', args=[self.habit.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(),
                         0)  # Проверяем, что количество объектов модели Habit равно 0,
        # что означает успешное удаление привычки.
