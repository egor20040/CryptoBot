from aiogram import types
from loader import dp, _


@dp.message_handler()
async def bot_echo(message: types.Message):
    text = _(
        'У меня нет такой команды.\n'
        'Попробуйте:\n'
        '/help - Получить справку\n'
    )
    await message.reply(text)
