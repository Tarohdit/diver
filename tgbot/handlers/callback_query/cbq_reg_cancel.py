from telebot import TeleBot
from telebot.types import CallbackQuery


def cbq_reg_cancel(call: CallbackQuery, bot: TeleBot):
    bot.answer_callback_query(callback_query_id=call.id, text="Вы отменили регистрацию", show_alert=True)
