from telebot import TeleBot
from telebot.types import CallbackQuery


def cbq_reg(call: CallbackQuery, bot: TeleBot):
    bot.answer_callback_query(callback_query_id=call.id, text="Успешная регистрация", show_alert=True)