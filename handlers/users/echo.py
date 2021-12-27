from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    text = [
        'У меня нет такой команды.',
        'Попробуйте:',
        '/help - Получить справку'
    ]
    await message.reply('\n'.join(text))
