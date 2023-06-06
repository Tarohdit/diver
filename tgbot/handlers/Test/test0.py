from telebot import TeleBot
from telebot.types import Message
from tgbot.states.Test.test import Test

def test0(message: Message, bot: TeleBot):
    """
    Стартовая команда. Здесь мы находимся в начальном состоянии
    """
    bot.set_state(message.from_user.id, Test.Q1, message.chat.id)
    bot.send_message(message.chat.id, "Привет, как тебя зовут?")
