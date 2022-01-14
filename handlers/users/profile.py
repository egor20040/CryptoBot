from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from documents.locate import DOC_DIR
from keyboards.inline.callback_datas import set_callback
from keyboards.inline.profile import keybord_profile, keybord_profile_main, keybord_profile_promo, keybord_back_profile
from loader import dp, _
import datetime as dt
from utils.db_api import quick_commands as commands


@dp.message_handler(text="🔐 Personal data", state='*')
async def show_menu_en(message: types.Message, state: FSMContext):
    await show_menu(message, state)


@dp.message_handler(text="🔐 Личные данные", state='*')
async def show_menu(message: types.Message, state: FSMContext):
    await state.finish()
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
        "Ваша реферальная ссылка: http://t.me/{bot_name}?start={user_id}\n\n"
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
    await message.answer(text, reply_markup=keybord_profile_main)


@dp.callback_query_handler(text="back_profile")
async def back_profile(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
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
        "Ваша реферальная ссылка: http://t.me/{bot_name}?start={user_id}\n\n"
        "🔒 Ваши данные защищены RSA-2048, DH-2048 и AES шифрованием."

    ).format(
        user_id=call.message.chat.id,
        btc=btc,
        eth=eth,
        sol=sol,
        qiwi=qiwi,
        days=start.days,
        bot_name=bot_user.username,
        invite=user.invited
    )
    await call.message.answer(text, reply_markup=keybord_profile_main)


@dp.callback_query_handler(text="add_wallet")
async def add_wallet(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    text = _(
        '💵 Добавить Кошелек\n\n'
        'Выберите кошелек, который хотите добавить.'

    )
    await call.message.answer(text, reply_markup=keybord_profile)


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


@dp.callback_query_handler(text="reports")
async def reports(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    f = open(DOC_DIR / "deals.csv", "rb")
    i = open(DOC_DIR / "lots.csv", "rb")
    l = open(DOC_DIR / "promocodes.csv", "rb")
    e = open(DOC_DIR / "transactions.csv", "rb")
    await dp.bot.send_document(chat_id=call.message.chat.id, document=f)
    await dp.bot.send_document(chat_id=call.message.chat.id, document=i)
    await dp.bot.send_document(chat_id=call.message.chat.id, document=l)
    await dp.bot.send_document(chat_id=call.message.chat.id, document=e)


@dp.callback_query_handler(text="promo")
async def reports(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    text = _(
        '🎟 Промокоды\n\n'
        '🎁 Здесь можно активировать промокод полученный у наших партнёров.'

    )
    await call.message.answer(text, reply_markup=keybord_profile_promo)


@dp.callback_query_handler(text='activate_promo')
async def show_activate(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await state.set_state("promo")
    text = _(
        "Ведите код"
    )
    await call.message.answer(text)


@dp.message_handler(state="promo")
async def update_currency(message: types.Message, state: FSMContext):
    text = _(
        "🚫 Данный промокод неверный, либо уже был использован"
    )
    await message.answer(text, reply_markup=keybord_profile_promo)
    await state.finish()


@dp.callback_query_handler(text='referral_savings')
async def show_activate(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    bot_user = await dp.bot.get_me()
    text = _(
        "💰 Реферальные накопления\n\n"
        "У вас нет реферальных накоплений.\n"
        "Пригласите друзей и получайте процент от общего количества сделок.\n\n"
        "Ваша реферальная ссылка: http://t.me/{bot_name}?start={user_id}"
    ).format(
        user_id=call.message.chat.id,
        bot_name=bot_user.username,
    )
    await call.message.answer(text, reply_markup=keybord_back_profile)
