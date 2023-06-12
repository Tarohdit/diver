from telebot import util    # для тега, ника пользователя в сообщение как ссылки на его аккаунт


class User:
    user_id = None
    user_name = None
    user_link = None  # ссылка на аккаунт пользователя, синий ник в чате

    def __init__(self, CallbackQuery):
        self.user_id = CallbackQuery.from_user.id  # номер пользователя который нажал на кнопку регистрации
        self.user_name = CallbackQuery.from_user.first_name  # имя пользователей который нажал на кнопку регистрации
        self.user_link = util.user_link(CallbackQuery.from_user)  # ссылка на аккаунт пользователя (синий ник в чате)


    def info(self):
        print(
            f'class User: user_id: {self.user_id}\n'
            f'class User: user_name: {self.user_name}\n'
            f'class User: user_link: {self.user_link}\n'
        )
