from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from keyboards.inline.callback_datas import set_callback
from keyboards.inline.profile import keybord_profile
from loader import dp, _
import datetime as dt
from utils.db_api import quick_commands as commands


@dp.message_handler(text="🔐 Personal data")
async def show_menu_en(message: types.Message):
    await show_menu(message)


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
    user_id = message.from_user.id
    text = _(
        "🔐 Личные данные\n\n"
        "Ваш id: {user_id}\n"
        "Всего сделок: 0\n"
        "Приглашенных пользователей: {invite}\n\n"
        "BTC кошелек: {btc}\n\n"
        "ETH кошелек: {eth}\n\n"
        "SOL кошелек: {sol}\n\n"
        "QIWI кошелек: {qiwi}\n\n"
        "Дней в сервисе: {days}\n\n"
        "Ваша ссылка для приглашения пользователей: http://t.me/{bot_name}?start={user_id}\n\n"
        "🔒 Ваши данные защищены RSA-2048, DH-2048 и AES шифрованием."

    ).format(
        user_id=user_id,
        btc=btc,
        eth=eth,
        sol=sol,
        qiwi=qiwi,
        days=start.days,
        bot_name=bot_user.username,
        invite=user.invited
    )
    await message.answer(text, reply_markup=keybord_profile)


@dp.callback_query_handler(set_callback.filter(text_name="purse"))
async def show_set_menu(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    currency = callback_data.get("purse")
    await state.update_data(currency=currency)
    await state.set_state("ask")
    text = _(
        "Введите номер кошелька  {currency}"
    ).format(
        currency=currency
    )
    await call.message.answer(text)


@dp.message_handler(state="ask")
async def update_currency(message: types.Message, state: FSMContext):
    data = await state.get_data()
    number = data.get("currency")
    await commands.update_purse(id=message.from_user.id, purse=message.text, currency=number)
    text = _(
        "Ваш {number} кошелек обновлен"
    ).format(
        number=number
    )
    await message.answer(text)
    await state.finish()
    await show_menu(message)
