from telebot import TeleBot
from telebot.types import Message


# неверный номер        # incorrect number
def test4(message: Message, bot: TeleBot):
    """
    Неверный ответ для MyStates.age
    Wrong response for MyStates.age
    """
    bot.send_message(message.chat.id, 'Похоже, вы отправляете строку в поле age. Пожалуйста, введите номер')
