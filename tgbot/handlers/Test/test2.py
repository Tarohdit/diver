from telebot import TeleBot
from telebot.types import Message
from tgbot.states.Test.test import Test

def test2(message: Message, bot: TeleBot):
    """
    Состояние 2. Будет обработано, если состояние пользователя — Test.Q2
    State 2. Will process when user's state is Test.Q2
    """
    bot.send_message(message.chat.id, "Ваш возраст?")
    bot.set_state(message.from_user.id, Test.Q3, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['surname'] = message.text
