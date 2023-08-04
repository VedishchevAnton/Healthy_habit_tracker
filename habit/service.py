import requests

from config import settings

telegram_api_token = settings.TELEGRAM_API_TOKEN
chat_id = settings.CHAT_ID
message = "Не забудь о своей привычке"

url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
params = {
    "chat_id": chat_id,
    "text": message
}

response = requests.get(url, params=params)
print(response.json())
