from telebot import TeleBot
from telebot.types import CallbackQuery
from tgbot.data.AllChats import AllChats
from tgbot.utils.edit_message_reg import edit_message_reg
from tgbot.data.Game import Game


def cbq_reg(call: CallbackQuery, bot: TeleBot):
    chat_id = call.message.chat.id
    obj_chat = AllChats.get_obj_chat(chat_id)
    exists = obj_chat.check_list(call)
    if exists == False:
        if obj_chat.get_amount_players() < Game.max_players:  # если кол-во игроков в реге меньше макс игроков для игры
            obj_chat.add_user(call)
            edit_message_reg(call, bot)
            bot.answer_callback_query(callback_query_id=call.id, text="Успешная регистрация", show_alert=True)  # уведомление (часики)
        else:
            bot.answer_callback_query(callback_query_id=call.id, text="Мест нет", show_alert=True)
    else:
        bot.answer_callback_query(callback_query_id=call.id, text="Вы уже зарегистрировались", show_alert=True)
