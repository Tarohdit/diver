from telebot import TeleBot
from telebot.types import CallbackQuery
from tgbot.data.list_reg_1 import AllChats
from tgbot.utils.edit_message_reg import edit_message_reg


def cbq_reg_cancel(call: CallbackQuery, bot: TeleBot):
    obj_chat = AllChats.get_obj_chat(call)
    exists = obj_chat.check_list(call)
    if exists == True:
        obj_chat.delete_user(call)
        edit_message_reg(call, bot)
        bot.answer_callback_query(callback_query_id=call.id, text="Вы отменили регистрацию", show_alert=True)
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="Вы еще не зарегистрировались", show_alert=True)
