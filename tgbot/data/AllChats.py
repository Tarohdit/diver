from tgbot.data.Chat import Chat


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
    def get_obj_chat(chat_id):
        for i in range(len(AllChats.list_all_chats)):  # завернуть в функцию def check_list
            __object = AllChats.list_all_chats[i]  # достать i элемент (объект класса Chat) из списка
            __chat_id = __object.chat_id  # класс Chat, свойство chat_id
            if chat_id == __chat_id:
                print('class AllChats: return object class Chat')
                return __object
