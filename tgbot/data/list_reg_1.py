from telebot import util    # для тега, ника пользователя в сообщение как ссылки на его аккаунт


class AllChats:
    list_all_chats = []

    @staticmethod
    def add_chat(chat_id):  # добавить чат в список чатов
        __exists = False
        for i in range(len(AllChats.list_all_chats)):  # завернуть в функцию def check_list
            __object = AllChats.list_all_chats[i]  # достать i элемент (объект класса Chat) из списка
            __chat_id = __object.get_chat_id()  # вызвать метод класса Chat, который вернет chat_id
            if chat_id == __chat_id:
                __exists = True  # чат с таким ид уже есть в списке
                print('class AllChats: такой чат уже есть')

        if __exists == False:  # если объекта с таким chat_id нет в списке
            print('class AllChats: добавить новый чат в список')
            chat = Chat(chat_id)  # создать объект класса Chat
            AllChats.list_all_chats.append(chat)  # добавить его в конец списка
        AllChats.info()


    @staticmethod
    def info():
        print(
            f'class AllChats: list_all_chats: {AllChats.list_all_chats}\n'  # показать какие чаты в списке
        )


    @staticmethod
    def get_obj_chat(CallbackQuery):
        chat_id = CallbackQuery.message.chat.id
        for i in range(len(AllChats.list_all_chats)):  # завернуть в функцию def check_list
            __object = AllChats.list_all_chats[i]  # достать i элемент (объект класса Chat) из списка
            __chat_id = __object.get_chat_id()  # вызвать метод класса Chat, который вернет chat_id
            if chat_id == __chat_id:
                print('class AllChats: return object class Chat')
                return __object


class Chat:
    chat_id = None
    list_users = []

    def __init__(self, chat_id):
        self.chat_id = chat_id
        print(f'class Chat: chat_id: {self.chat_id}')  # или print(self.__class__.__name__)  # Chat
        # возможно удалить
        print(self)  # показать объект


    def info(self):
        print(
            f'class Chat: chat_id: {self.chat_id}\n'
            f'class Chat: list_users: {self.list_users}\n'   # показать что в списке
        )


    def get_chat_id(self):
        return self.chat_id


    def add_user(self, CallbackQuery):  # добавить игрока в рег список
        user_id = CallbackQuery.from_user.id  # номер пользователя который нажал на кнопку регистрации
        __exists = False
        # завернуть в функцию def check_list
        for i in range(len(self.list_users)):  # пробежаться по списку игроков
            __object = self.list_users[i]  # достать i элемент (объект класса User) из списка
            __user_id = __object.get_user_id()  # вызвать метод класса User, который вернет user_id
            if user_id == __user_id:
                __exists = True  # игрок с таким ид уже есть в списке
                print('class Chat: игрок уже зарегистрирован')

        if __exists == False:  # если объекта с таким user_id нет в списке
            print('class Chat: добавить нового игрока в рег список')
            user = User(CallbackQuery)  # создать объект класса User
            self.list_users.append(user)  # добавить его в конец списка
        self.info()


class User:
    user_id = None
    user_name = None
    user_link = None

    def __init__(self, CallbackQuery):
        print(CallbackQuery)
        self.user_id = CallbackQuery.from_user.id  # номер пользователя который нажал на кнопку регистрации
        self.user_name = CallbackQuery.from_user.first_name  # имя пользователей который нажал на кнопку регистрации
        self.user_link = util.user_link(CallbackQuery.from_user)  # ссылка на аккаунт пользователя (синий ник в чате)


    def info(self):
        print(
            f'class User: user_id: {self.user_id}\n'
            f'class User: user_name: {self.user_name}\n'
            f'class User: user_link: {self.user_link}\n'
        )


    def get_user_id(self):
        return self.user_id
