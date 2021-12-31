from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from typing import Tuple, Any
from data.config import I18N_DOMAIN
from locales.locate import LOCALES_DIR

from utils.db_api import quick_commands as commands


async def get_lang(user_id):
    # Делаем запрос к базе, узнаем установленный язык
    user = await commands.select_user(user_id)
    if user:
        # Если пользователь найден - возвращаем его
        return user.language


class ACLMiddleware(I18nMiddleware):
    # Каждый раз, когда нужно узнать язык пользователя - выполняется эта функция
    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        # Возвращаем язык из базы ИЛИ (если не найден) - язык из Телеграма
        return await get_lang(user.id)


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        """
        User locale getter
        You can override the method if you want to use different way of getting user language.
        :param action: event name
        :param args: event arguments
        :return: locale name
        """
        user: types.User = types.User.get_current()
        if user.language_code == 'ru':
            language = 'ru'
        else:
            language = 'en'

        return await get_lang(user.id) or language


def setup_middleware(dp):
    # Устанавливаем миддлварь
    i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    _ = i18n.lazy_gettext
    return _
