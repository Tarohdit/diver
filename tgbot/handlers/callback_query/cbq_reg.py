from telebot import TeleBot
from telebot.types import CallbackQuery
from tgbot.data.list_reg_1 import AllChats
from tgbot.keyboards.keyb_reg import keyb_reg

def cbq_reg(call: CallbackQuery, bot: TeleBot):
    obj_chat = AllChats.get_obj_chat(call)
    exists = obj_chat.check_list(call)
    if exists == False:
        obj_chat.add_user(call)
        edit_massage(call, bot, obj_chat)
        bot.answer_callback_query(callback_query_id=call.id, text="Успешная регистрация", show_alert=True)  # уведомление (часики)
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="Вы уже зарегистрировались", show_alert=True)


def edit_massage(call: CallbackQuery, bot: TeleBot, obj_chat):  # отредактировать сообщение
    chat_id = call.message.chat.id
    message_id = call.message.message_id
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
    # print(string)
    return string
