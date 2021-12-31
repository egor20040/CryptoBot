import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hlink

from keyboards.default.main_menu import main_menu
from keyboards.default.start import start
from loader import dp, _
from utils.db_api import quick_commands as commands


@dp.message_handler(CommandStart(deep_link=re.compile("[0-9]+")))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    print(deep_link_args)
    user = await commands.select_user(message.from_user.id)
    if user:
        await message.answer(_("Выберете категорию которая вам нужна ниже:"), reply_markup=main_menu)
    else:
        try:
            user = await commands.select_user(int(deep_link_args))
            count = int(user.invited) + 1
            await commands.update_invited(int(deep_link_args), int(count))
        except:
            pass
        if message.from_user.language_code == 'ru':
            currency = "RUB"
            language = 'ru'
        else:
            currency = "USD"
            language = 'en'
        await commands.add_user(id=message.from_user.id, name=message.from_user.full_name, chat_id=message.chat.id,
                                language=language, currency=currency, invited=0,
                                called=int(deep_link_args))
        text = _(
            'Привет, {name}!'
        ).format(
            name=message.from_user.full_name
        )
        await message.answer(text)
        text1 = _(
            'Вы подтверждаете, что ознакомились и согласны с {custom}?'
        ).format(
            custom=hlink(_("условиями предоставления услуг"), "https://bitzlato.com/terms-of-service-bitzlato/")
        )
        await message.answer(text1, reply_markup=start, disable_web_page_preview=True)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    if user:
        await message.answer(_("Выберете категорию которая вам нужна ниже:"), reply_markup=main_menu)
    else:
        if message.from_user.language_code == 'ru':
            currency = "RUB"
            language = 'ru'
        else:
            currency = "USD"
            language = 'en'
        await commands.add_user(id=message.from_user.id, name=message.from_user.full_name, chat_id=message.chat.id,
                                language=language, currency=currency, invited=0)
        text = _(
            'Привет, {name}!'
        ).format(
            name=message.from_user.full_name
        )
        await message.answer(text)
        text1 = _(
            'Вы подтверждаете, что ознакомились и согласны с {custom}?'
        ).format(
            custom=hlink(_("условиями предоставления услуг"), "https://bitzlato.com/terms-of-service-bitzlato/")
        )
        await message.answer(text1, reply_markup=start, disable_web_page_preview=True)
