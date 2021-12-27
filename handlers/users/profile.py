from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from keyboards.inline.callback_datas import set_callback
from keyboards.inline.profile import keybord_profile
from loader import dp
import datetime as dt
from utils.db_api import quick_commands as commands


@dp.message_handler(text="🔐 Личные данные")
async def show_menu(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    bot_user = await dp.bot.get_me()
    btc = ''
    eth = ''
    qiwi = ''
    sol = ''
    if user.btc:
        btc = user.btc
    if user.eth:
        eth = user.eth
    if user.qiwi:
        qiwi = user.qiwi
    if user.sol:
        sol = user.sol

    now = dt.datetime.utcnow()
    created_at = user.created_at + dt.timedelta(hours=3)
    moscow_now = now + dt.timedelta(hours=3)
    start = moscow_now.date() - created_at.date()
    text = [
        f'🔐 Личные данные',
        f'',
        f'{hbold("Ваш id:")} {message.from_user.id}',
        f'{hbold("Всего сделок:")} 0',
        f'{hbold("Приглашенных пользователей:")} {user.invited}',
        '',
        f'BTC кошелек: {btc}',
        '',
        f'ETH кошелек: {eth}',
        '',
        f'SOL кошелек: {sol}',
        '',
        f'QIWI кошелек: {qiwi}',
        f'',
        f'{hbold("Дней в сервисе:")} {start.days}',
        f'',
        f'Ваша ссылка для приглашения пользователей: http://t.me/{bot_user.username}?start={message.from_user.id}',
        f'',
        f'🔒 Ваши данные защищены RSA-2048, DH-2048 и AES шифрованием.',

    ]
    await message.answer('\n'.join(text), reply_markup=keybord_profile)


@dp.callback_query_handler(set_callback.filter(text_name="purse"))
async def show_set_menu(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    currency = callback_data.get("purse")
    await state.update_data(currency=currency)
    await state.set_state("ask")
    await call.message.answer(f"Введите номер кошелька  {currency}")


@dp.message_handler(state="ask")
async def update_currency(message: types.Message, state: FSMContext):
    data = await state.get_data()
    number = data.get("currency")
    await commands.update_purse(id=message.from_user.id, purse=message.text, currency=number)
    await message.answer(f"Ваш {number} кошелек обновлен")
    await state.finish()
    await show_menu(message)
