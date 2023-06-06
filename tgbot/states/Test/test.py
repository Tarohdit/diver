from telebot.handler_backends import State, StatesGroup

# Группа состояний.          # States group.
class Test(StatesGroup):  # класс Test наследует класс StatesGroup (группу состояний)
    # Просто назовите переменные по-другому             # Just name variables differently
    Q1 = State()    # Отдельное состояние - фильтр State, для хендлеров,
    Q2 = State()    # с этого момента достаточно создавать экземпляры класса State
    Q3 = State()    # creating instances of State class is enough from now
