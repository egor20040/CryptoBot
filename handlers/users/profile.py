from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import set_callback
from keyboards.inline.profile import keybord_profile
from loader import dp


@dp.message_handler(text="🔐 Личные данные")
async def show_menu(message: types.Message):
    text = [
        f'Ваш id: {message.from_user.id}',
        'Всего седлок: 0',
        'Приглашеных пользователей: 0',
        'BTC кошелек: ',
        'ETH кошелек: ',
        'SOL кошелек: ',
        'QIWI кошелек: '
    ]
    await message.answer('\n'.join(text), reply_markup=keybord_profile)


@dp.callback_query_handler(set_callback.filter(text_name="purse"))
async def show_set_menu(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    currency = callback_data.get("purse")
    await call.message.answer(f"Вы задаете {currency}")
