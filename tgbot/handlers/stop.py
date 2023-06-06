from telebot import TeleBot
from telebot.types import Message

def cmd_stop(message: Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Бот остановлен")