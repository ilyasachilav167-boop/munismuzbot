import telebot
import os

# Render sozlamalaridan tokenni oladi
TOKEN = os.getenv("BOT_TOKEN") 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    text = (
        f"Assalomu alaykum, {user_name}!\n"
        "🎶 Musiqa izlash botiga xush kelibsiz.\n"
        "🌟 Hamkorimiz: @munisaparfumerie\n"
        "Musiqa topish uchun qo‘shiq nomini yozing."
    )
    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"'{message.text}' bo‘yicha musiqa qidirilmoqda...")

if __name__ == "__main__":
    bot.infinity_polling()

