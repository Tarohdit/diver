from telebot import TeleBot
from telebot.types import Message


def cmd_help(message: Message, bot: TeleBot):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Помощь')
