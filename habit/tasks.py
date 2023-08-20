from celery import shared_task
from datetime import datetime, time, timedelta
import requests

from config import settings
from habit.models import Habit

telegram_api_token = settings.TELEGRAM_API_TOKEN
chat_id = settings.CHAT_ID


@shared_task
def send_telegram_message(habit_id):
    # Получаем привычку по ее id
    habit = Habit.objects.get(id=habit_id)
    # Получаем время, когда нужно выполнить привычку
    habit_time = habit.time
    # Получаем текущее время
    now = datetime.now().time()
    # Вычисляем количество секунд до нужного времени выполнения привычки
    seconds_until_habit = (datetime.combine(datetime.today(), habit_time) - datetime.combine(datetime.today(),
                                                                                             now)).total_seconds()
    # Отправляем сообщение пользователю через телеграм
    message = (f"Напоминание о привычке для пользователя {habit.user.telegram_username}:\nМесто: {habit.place}\n"
               f"Действие: {habit.action}\nВремя: {habit.time}")
    url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
        "schedule_date": int(now.timestamp() + seconds_until_habit)
    }
    response = requests.get(url, params=params)
