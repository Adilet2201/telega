import telebot
from telebot import types
import os

# Твой токен
TOKEN = os.environ.get("Token")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # Приветствие
    text = (
        "Сәлем, студент! 🎓\n\n"
        "Сізді біздің *TULGA* клубына қосылуға шақырамыз!\n\n"
        "📚 Бір семестр ішінде біз мыналарды үйренеміз:\n"
        "• Мақсатқа жету жолдары\n"
        "• Қаржылық сауаттылық\n"
        "• Университетте жақсы баға алудың құпиялары\n"
        "• Жаңа ортада өз орныңды табу және өзің болу\n\n"
        "💡 Барлығы студентке пайдалы дағдылар!"
    )

    markup = types.InlineKeyboardMarkup()
    
    # Клубқа тіркелу батырмасы
    join_button = types.InlineKeyboardButton(
        text="📋 Клубқа тіркелу",
        url="https://telega-production-4707.up.railway.app/"
    )
    
    # Бағдарлама батырмасы
    program_button = types.InlineKeyboardButton(
        text="📘 Бағдарлама",
        callback_data="program"
    )
    
    markup.add(join_button)
    markup.add(program_button)

    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

# Обработчик нажатия на "Бағдарлама"
@bot.callback_query_handler(func=lambda call: call.data == "program")
def show_program(call):
    program_text = (
        "*TULGA клубының бағдарламасы:*\n\n"
        "1️⃣ Мақсат қою және оған жету стратегиялары\n"
        "2️⃣ Қаржылық сауаттылық негіздері\n"
        "3️⃣ Университетте сәтті оқу лайфхактары\n"
        "4️⃣ Тайм-менеджмент және өнімділік\n"
        "5️⃣ Жаңа ортада өз орныңды табу\n"
        "6️⃣ Өзін-өзі дамыту әдістері\n\n"
        "🔥 Бұл дағдылар сіздің өміріңізде ұзақ уақыт бойы пайдасын береді!"
    )
    bot.send_message(call.message.chat.id, program_text, parse_mode="Markdown")

# Запуск бота
print("Bot is running...")
bot.polling(none_stop=True)
