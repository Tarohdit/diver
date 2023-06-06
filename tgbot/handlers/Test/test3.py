from telebot import TeleBot
from telebot.types import Message


# результат     # result
def test3(message: Message, bot: TeleBot):
    """
    Состояние 3. Будет обработано, когда состояние пользователя будет Test.Q3
    State 3. Will process when user's state is Test.Q3
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Готово, смотри:\n<b>"
               f"Name: {data['name']}\n"
               f"Surname: {data['surname']}\n"
               f"Age: {message.text}</b>")
        bot.send_message(message.chat.id, msg, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)
