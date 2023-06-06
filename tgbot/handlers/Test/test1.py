from telebot import TeleBot
from telebot.types import Message
from tgbot.states.Test.test import Test


def test1(message: Message, bot: TeleBot):
    """
    Состояние 1. Будет обработано, если состояние пользователя — Test.Q1
    State 1. Will process when user's state is Test.Q1
    """
    bot.send_message(message.chat.id, 'Теперь напиши мне фамилию')
    bot.set_state(message.from_user.id, Test.Q2, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
