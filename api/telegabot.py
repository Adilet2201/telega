import json
import os

BOT_TOKEN = "7225020257:AAGfcF94WYhuqAA8NDb-DwYABj0zDKBkM-k"
ADMIN_CHAT_ID = ""  # можно отправлять админу

def handler(request):
    if request.method == "POST":
        try:
            data = request.json
            name = data.get("name")
            instagram = data.get("instagram")
            receipt = data.get("receipt")

            message = (
                f"Новая регистрация на конкурс:\n"
                f"👤 Имя: {name}\n"
                f"📸 Instagram: @{instagram}\n"
                f"🧾 Чек: {receipt}"
            )

            import requests
            telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": ADMIN_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            }
            r = requests.post(telegram_url, json=payload)

            return {
                "statusCode": 200,
                "headers": { "Content-Type": "text/plain" },
                "body": "Спасибо! Вы зарегистрированы 🎉"
            }

        except Exception as e:
            return {
                "statusCode": 500,
                "headers": { "Content-Type": "text/plain" },
                "body": f"Ошибка: {str(e)}"
            }

    return {
        "statusCode": 405,
        "headers": { "Allow": "POST" },
        "body": "Метод не разрешен"
    }
