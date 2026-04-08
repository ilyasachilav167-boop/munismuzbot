import telebot
import os

# Telegram bot tokeningiz
TOKEN = '7629555193:AAHkC869Wq_Vl867eS7t65F3_6eZ-wU80'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        f"Assalomu alaykum, {message.from_user.first_name}!\n\n"
        "🎶 Musiqa izlash botiga xush kelibsiz.\n\n"
        "🌟 Hamkorimiz: @munisaparfumerie — Eng sifatli atirlar olami!\n"
        "Musiqa topish uchun qo'shiq nomini yozing."
    )
    bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"'{message.text}' bo'yicha musiqa qidirilmoqda...\n\nSifatli iforlar: @munisaparfumerie")

if __name__ == "__main__":
    bot.infinity_polling()
