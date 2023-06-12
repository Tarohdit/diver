from telebot import TeleBot
from telebot.types import Message
from tgbot.data.AllChats import AllChats
from tgbot.keyboards.keyb_reg import keyb_reg


def registration(message: Message, bot: TeleBot):
    chat_id = message.chat.id
    AllChats.add_chat(chat_id)
    obj_chat = AllChats.get_obj_chat(chat_id)
    obj_chat.clear_list_users()  # при повторном вызове команды reg очистить список игроков
    bot.send_message(chat_id,
            'Ведется набор в игру\n'
            'Кол-во игроков 2-6',
            reply_markup=keyb_reg())
