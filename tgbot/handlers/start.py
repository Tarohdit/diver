from telebot import TeleBot
from telebot.types import Message

from tgbot.data.AllChats import AllChats
from tgbot.data.Game import Game
from tgbot.handlers.registration import registration


def cmd_start(message: Message, bot: TeleBot):
    chat_id = message.chat.id
    AllChats.add_chat(chat_id)
    check_number_players(chat_id, message, bot)


def check_number_players(chat_id, message: Message, bot: TeleBot):  # проверка кол-ва игроков
    obj_chat = AllChats.get_obj_chat(chat_id)
    amount_players = obj_chat.get_amount_players()
    if Game.min_players <= amount_players <= Game.max_players:
        bot.send_message(chat_id, "Игра запущена")  # начать игру
        Game.start()
    else:
        registration(message, bot)  # запустить регистрацию
