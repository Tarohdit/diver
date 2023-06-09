# filters
from tgbot.filters.admin_filter import AdminFilter
# Test
from tgbot.filters.Test.test_filter import StateFilter
from tgbot.filters.Test.test_filter import IsDigitFilter
# ===

# handlers
from tgbot.handlers.admin import admin_user
from tgbot.handlers.spam_command import anti_spam
from tgbot.handlers.user import any_user
from tgbot.handlers.stop import cmd_stop
# Test
from tgbot.handlers.Test.any_state import any_state
from tgbot.handlers.Test.test0 import test0
from tgbot.handlers.Test.test1 import test1
from tgbot.handlers.Test.test2 import test2
from tgbot.handlers.Test.test3 import test3
from tgbot.handlers.Test.test4 import test4
# ===
from tgbot.handlers.registration import registration
from tgbot.handlers.callback_query.cbq_reg import cbq_reg
from tgbot.handlers.callback_query.cbq_reg_cancel import cbq_reg_cancel

# middlewares
from tgbot.middlewares.antiflood_middleware import antispam_func

# models


# states
# Test
from tgbot.states.state_storage import state_storage
from tgbot.states.Test.test import Test
# ===

# utils
# from tgbot.utils.database import Database
from tgbot.utils.set_default_commands import set_default_commands
from tgbot.utils.welcome_message import welcome_message

# telebot
from telebot import TeleBot

# config
from tgbot import config

# db = Database()

# remove this if you won't use middlewares:
from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True

# I recommend increasing num_threads
#  передать хранилище боту (state_storage)
bot = TeleBot(config.TOKEN, num_threads=5, state_storage=state_storage)

set_default_commands(bot)
welcome_message(bot)

def register_handlers():
    bot.register_message_handler(admin_user, commands=['start'], admin=True, pass_bot=True)
    bot.register_message_handler(any_user, commands=['start'], admin=False, pass_bot=True)
    bot.register_message_handler(anti_spam, commands=['spam'], pass_bot=True)
    bot.register_message_handler(cmd_stop, commands=['stop'], pass_bot=True)
    # Test
    bot.register_message_handler(test0, commands=['test'], pass_bot=True)
    bot.register_message_handler(any_state, state="*", commands=['cancel'], pass_bot=True)
    bot.register_message_handler(test1, state=Test.Q1, pass_bot=True)
    bot.register_message_handler(test2, state=Test.Q2, pass_bot=True)
    bot.register_message_handler(test3, state=Test.Q3, is_digit=True, pass_bot=True)
    bot.register_message_handler(test4, state=Test.Q3, is_digit=False, pass_bot=True)
    # ===
    bot.register_message_handler(registration, commands=['reg'], pass_bot=True)
    bot.register_callback_query_handler(cbq_reg, func=lambda call: call.data=='reg', pass_bot=True)
    bot.register_callback_query_handler(cbq_reg_cancel, func=lambda call: call.data=='reg_cancel', pass_bot=True)

register_handlers()

# Middlewares
bot.register_middleware_handler(antispam_func, update_types=['message'])


# custom filters   # пользовательские фильтры, регистрация фильтров
bot.add_custom_filter(AdminFilter())
# Test
bot.add_custom_filter(IsDigitFilter())
bot.add_custom_filter(StateFilter(bot))
# ===

def run():
    bot.infinity_polling()


run()
