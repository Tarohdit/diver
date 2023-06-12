# стандартные команды для бота, обновляются при запуске бота
# /reg - Регистрация в игру
# /start - Начать игру
# /stop - Остановить бота

from telebot import TeleBot
from telebot import types

print('LOAD', str(__name__))

def set_default_commands(bot: TeleBot):
    bot.set_my_commands(
        [
            types.BotCommand('reg', 'Регистрация в игру'),
            types.BotCommand('start', 'Начать игру'),
            types.BotCommand('stop', 'Остановить бота'),
            types.BotCommand('spam', 'Проверить АнтиСпам'),
            types.BotCommand('test', 'Запустить тест состояний (state)'),
            types.BotCommand('cancel', 'Сбросить состояние'),
            types.BotCommand('help', 'Помощь'),
        ]
    )
    print('Команды бота обновлены')
    cmd = bot.get_my_commands()
    for i in range(len(cmd)):
        print(f'{cmd[i].command} - {cmd[i].description}')
    print()
