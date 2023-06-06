from telebot.custom_filters import SimpleCustomFilter
from tgbot.models.users_model import Admin


class AdminFilter(SimpleCustomFilter):
    """
    Filter for admin users
    """

    key = 'admin'
    def check(self, message):
        """
        RU когда пользователь пишет в личку боту, этот фильтр срабатывает
        EN when a user writes a private message to a bot, this filter is triggered
        chat id == user id
        """
        return int(message.chat.id) == int(Admin.ADMIN.value)