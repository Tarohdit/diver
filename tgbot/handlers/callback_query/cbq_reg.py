from telebot import TeleBot
from telebot.types import CallbackQuery
from tgbot.data.list_reg_1 import AllChats

def cbq_reg(call: CallbackQuery, bot: TeleBot):
    obj_chat = AllChats.get_obj_chat(call)
    obj_chat.add_user(call)

    bot.answer_callback_query(callback_query_id=call.id, text="Успешная регистрация", show_alert=True)  # уведомление (часики)
