from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hlink

from keyboards.default.start import start
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.answer(
        f'Вы подтверждаете, что ознакомились и согласны с {hlink("условиями предоставления услуг", "https://bitzlato.com/terms-of-service-bitzlato/")}?',
        reply_markup=start, disable_web_page_preview=True)
