from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import pandas as pd
import json
import os

# 🔁 Заменить на свои данные:
BOT_TOKEN = "7225020257:AAGfcF94WYhuqAA8NDb-DwYABj0zDKBkM-k"  # ← вставь сюда токен от BotFather
WEBAPP_FORM_URL = "https://yourdomain.com/form.html"  # ← ссылка на HTML-форму

CSV_FILENAME = "registrations.csv"

# Создать файл, если не существует
if not os.path.exists(CSV_FILENAME):
    pd.DataFrame(columns=["user_id", "username", "name", "instagram", "check"]).to_csv(CSV_FILENAME, index=False)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("📋 Зарегистрироваться", web_app=WebAppInfo(url=WEBAPP_FORM_URL))]]
    await update.message.reply_text(
        "👋 Привет! Участвуй в розыгрыше машины!\n\nНажми кнопку ниже и заполни форму 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Принимаем данные из WebApp
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = json.loads(update.message.web_app_data.data)

        df = pd.DataFrame([{
            "user_id": update.message.from_user.id,
            "username": update.message.from_user.username or "",
            "name": data.get("name", ""),
            "instagram": data.get("instagram", ""),
            "check": data.get("check", "")
        }])

        df.to_csv(CSV_FILENAME, mode='a', header=False, index=False)
        await update.message.reply_text("✅ Успешно зарегистрировано. Удачи!")
    except Exception as e:
        print("Ошибка:", e)
        await update.message.reply_text("⚠️ Ошибка при регистрации.")


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
print("🚀 Бот запущен...")
app.run_polling()
