import os
import telebot
from dotenv import load_dotenv 
load_dotenv(r'E:\theatrbot\.env')
TOKEN = os.getenv('BOT_TOKEN')


bot = telebot.TeleBot(ТОКЕН )
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Доступные команды: /start, /help")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Бот жив! Отправьте 'тишина', 'время', 'вечер', 'ночь' или 'пространство'.")

@bot.message_handler(content_types=['text'])
def reply_to_word(message):
    user_text = message.text.lower()
    if "тишина" in user_text:
        bot.reply_to(message, "Тишина — это пространство между мыслями")
    if "время" in user_text:
        bot.reply_to(message, "Время — это ткань, из которой соткана реальность")
    if "вечер" in user_text:
        bot.reply_to(message, "Вечер — это время, из которого изъяли спешку")
    if "ночь" in user_text:  # <-- Исправлено: было "Ночь"
        bot.reply_to(message, "Ночь — это чёрный бархат, на котором звёзды вышивают свои истории")
    if "пространство" in user_text:  # <-- Исправлено: было "Пространство"
        bot.reply_to(message, "Пространство — сцена для несыгранных диалогов")

bot.polling(none_stop=True, interval=0)