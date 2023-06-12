from telebot import TeleBot
from telebot.types import CallbackQuery
from tgbot.data.AllChats import AllChats
from tgbot.keyboards.keyb_reg import keyb_reg


def edit_message_reg(call: CallbackQuery, bot: TeleBot):  # отредактировать сообщение
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    obj_chat = AllChats.get_obj_chat(chat_id)
    list_link = obj_chat.list_user_link()
    bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                          text=f"Ведется набор в игру\n"
                               f"Кол-во игроков 2-6\n"
                               f"Зарегистрировались:\n\n"
                               f"{list_pillars(list_link)}",
                          reply_markup=keyb_reg(),
                          parse_mode='html')


def list_pillars(list_A):  # список в столбик с порядковым номером (i+1)
    string = ''
    for i in range(len(list_A)):
        string += str(i+1) + ' ' + str(list_A[i]) + '\n'
    return string
