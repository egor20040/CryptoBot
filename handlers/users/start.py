from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hlink

from keyboards.default.main_menu import main_menu
from keyboards.default.start import start
from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    if user:
        await message.answer("Выберете категорию которая вам нужна ниже:", reply_markup=main_menu)
    else:
        if message.from_user.language_code == 'ru':
            currency = "RUB"
        else:
            currency = "USD"
        await commands.add_user(id=message.from_user.id, name=message.from_user.full_name, chat_id=message.chat.id,
                                language=message.from_user.language_code, currency=currency)
        await message.answer(f'Привет, {message.from_user.full_name}!')
        await message.answer(
            f'Вы подтверждаете, что ознакомились и согласны с {hlink("условиями предоставления услуг", "https://bitzlato.com/terms-of-service-bitzlato/")}?',
            reply_markup=start, disable_web_page_preview=True)
