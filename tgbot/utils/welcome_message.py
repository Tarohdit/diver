from tgbot.models.users_model import Admin
from telebot import TeleBot

print('LOAD', str(__name__))


def welcome_message(bot: TeleBot):
    """
    RU бот сообщает админам что он запущен
    EN bot informs the admins that it is running
    """
    chat_id = int(Admin.ADMIN.value)
    bot.send_message(chat_id, "Бот запущен")
