from telebot import TeleBot
from telebot.types import CallbackQuery
from tgbot.data.list_reg_1 import AllChats
from tgbot.utils.edit_message_reg import edit_message_reg


def cbq_reg(call: CallbackQuery, bot: TeleBot):
    obj_chat = AllChats.get_obj_chat(call)
    exists = obj_chat.check_list(call)
    if exists == False:
        if obj_chat.get_list_length() < 6:  # если кол-во игроков в реге меньше макс игроков для игры
            obj_chat.add_user(call)
            edit_message_reg(call, bot)
            bot.answer_callback_query(callback_query_id=call.id, text="Успешная регистрация", show_alert=True)  # уведомление (часики)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="Мест нет", show_alert=True)
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="Вы уже зарегистрировались", show_alert=True)
