from telebot import TeleBot
from telebot.types import Message
from tgbot.data.AllChats import AllChats
from tgbot.keyboards.keyb_reg import keyb_reg


def registration(message: Message, bot: TeleBot):
    AllChats.add_chat(message.chat.id)
    bot.send_message(message.chat.id,
            'Ведется набор в игру\n'
            'Кол-во игроков 2-6',
            reply_markup=keyb_reg())
