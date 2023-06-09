from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def keyb_reg():
    markup = InlineKeyboardMarkup()  # создаем клаву markup
    button1 = InlineKeyboardButton('Регистрация', callback_data='reg')  # создаем кнопку
    button2 = InlineKeyboardButton('Отмена', callback_data='reg_cancel')
    markup.add(button1, button2)  # добавляем к клаве кнопку в виде параметра
    return markup   # чтобы появилась клава с кнопками
