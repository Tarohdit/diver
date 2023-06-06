from telebot import TeleBot
from telebot.types import Message

# Любое состояние           # Any state
def any_state(message: Message, bot: TeleBot):
    """
    Состояние отмены     Cancel state
    """
    bot.send_message(message.chat.id, "Ваше состояние было отменено.")
    bot.delete_state(message.from_user.id, message.chat.id)
