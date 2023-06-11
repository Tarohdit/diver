from telebot import util    # для тега, ника пользователя в сообщение как ссылки на его аккаунт


class AllChats:
    list_all_chats = []

    @staticmethod
    def add_chat(chat_id):
        """
        RU Добавить чат в список чатов
        EN Add chat to chat list
        """
        __exists = False
        for i in range(len(AllChats.list_all_chats)):  # завернуть в функцию def check_list
            __object = AllChats.list_all_chats[i]  # достать i элемент (объект класса Chat) из списка
            __chat_id = __object.chat_id  # класс Chat, свойство chat_id
            if chat_id == __chat_id:
                print('class AllChats: такой чат уже есть')
                __exists = True  # чат с таким ид уже есть в списке
                __object.clear_list_users()  # при повторном вызове команды reg очистить список игроков

        if __exists == False:  # если объекта с таким chat_id нет в списке
            print('class AllChats: добавить новый чат в список')
            chat = Chat(chat_id)  # создать объект класса Chat
            AllChats.list_all_chats.append(chat)  # добавить его в конец списка
        AllChats.info()


    @staticmethod
    def info():
        print(
            f'class AllChats: list_all_chats: elements: {len(AllChats.list_all_chats)}, {AllChats.list_all_chats}\n'  # показать какие чаты в списке
        )


    @staticmethod
    def get_obj_chat(CallbackQuery):
        chat_id = CallbackQuery.message.chat.id
        for i in range(len(AllChats.list_all_chats)):  # завернуть в функцию def check_list
            __object = AllChats.list_all_chats[i]  # достать i элемент (объект класса Chat) из списка
            __chat_id = __object.chat_id  # класс Chat, свойство chat_id
            if chat_id == __chat_id:
                print('class AllChats: return object class Chat')
                return __object


class Chat:
    chat_id = None
    __list_users = []

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.__list_users = []  # сбросить список при создание нового объекта, когда новый чат добавляется в AllChats (антибаг 1)
        self.info()


    def info(self):
        print(
            'info\n'
            f'class Chat: chat_id: {self.chat_id}\n'
            f'class Chat: list_users: elements: {len(self.__list_users)}, {self.__list_users}\n'   # показать что в списке
        )


    def check_list(self, CallbackQuery):
        """
        RU Проверить содержит ли список объект, возвращается True или False
        EN Check if the list contains an object, returns True or False
        """
        user_id = CallbackQuery.from_user.id  # номер пользователя который нажал на кнопку (InlineKeyboardButton)
        __exists = False
        for i in range(len(self.__list_users)):  # пробежаться по списку игроков
            __object = self.__list_users[i]  # достать i элемент (объект класса User) из списка
            __user_id = __object.user_id  # класс User, свойство user_id
            if user_id == __user_id:
                __exists = True  # игрок с таким ид уже есть в списке
                print('class Chat: игрок есть в рег списке')

        if __exists == False:  # если объекта с таким user_id нет в списке
            print('class Chat: игрока нет в рег списке')

        return __exists


    def add_user(self, CallbackQuery):
        """
        RU Добавить игрока в рег список
        EN Add player to reg list
        """
        print('class Chat: добавить игрока в рег список')
        user = User(CallbackQuery)  # создать объект класса User
        self.__list_users.append(user)  # добавить его в конец списка
        self.info()


    def delete_user(self, CallbackQuery):
        """
        RU Удалить игрока из рег списка
        EN Remove player from reg list
        """
        user_id = CallbackQuery.from_user.id  # номер пользователя который нажал на кнопку (InlineKeyboardButton)
        for i in range(len(self.__list_users)):  # пробежаться по списку игроков
            __object = self.__list_users[i]  # достать i элемент (объект класса User) из списка
            if user_id == __object.user_id:  # класс User, свойство user_id
                print('class Chat: удалить игрока из рег списка')
                # remove() — удаляет первый встреченный элемент в списке, который соответствует условию.
                self.__list_users.remove(__object)
                break


    def list_user_link(self):
        """
        RU  возвращает список user_link зарегистрированных игроков
        EN returns user link list of registered players
        """
        __list_link = []  # временно хранит user_link
        for i in range(len(self.__list_users)):  # пробежаться по списку игроков
            __object = self.__list_users[i]  # достать i элемент (объект класса User) из списка
            __user_link = __object.user_link  # класс User, свойство user_link
            __list_link.append(__user_link)
        return __list_link


    def clear_list_users(self):
        self.__list_users.clear()  # clear удаляет все элементы списка
        print('class Chat: clear_list_users')


    def get_list_length(self):  # возвращает длину списка
        list_len = len(self.__list_users)
        return list_len


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
