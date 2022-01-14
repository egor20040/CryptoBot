from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default import main_menu
from keyboards.inline.callback_datas import set_volute, set_language
from keyboards.inline.settings import keybord_course, keybord_settings_back, keybord_currency, keybord_language
from loader import dp, _
from aiogram.utils.markdown import hlink
from utils.db_api import quick_commands as commands

from utils.misc.binance import StockExchange


@dp.message_handler(text="🛠 Settings", state='*')
async def show_menu_en(message: types.Message, state: FSMContext):
    await show_menu(message, state)


@dp.message_handler(text="🛠 Настройки", state='*')
async def show_menu(message: types.Message, state: FSMContext):
    await state.finish()
    text = _(
        '🛠 Настройки\n\n'
        'Ваш id: {user_id}\n\n'
        'Что Вы хотите изменить?'
    ).format(
        user_id=message.from_user.id
    )
    await message.answer(text, reply_markup=keybord_course)


@dp.callback_query_handler(text="backsettings")
async def show_back_menu_settings(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    text = _(
        '🛠 Настройки\n\n'
        'Ваш id: {user_id}\n\n'
        'Что Вы хотите изменить?'
    ).format(
        user_id=call.message.from_user.id
    )
    await call.message.answer(text, reply_markup=keybord_course)


@dp.callback_query_handler(text="course")
async def course(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    crypto = StockExchange()
    text = _(
        '📊 Курс\n\n'
        'Текущий курс:\n\n'
        '1 BTC = {btc}.0 RUB\n'
        '1 ETH = {eth}.0 RUB\n'
        '1 SOL = {sol}.0 RUB\n\n'
        'Текущий источник: {binance}'
    ).format(
        btc=crypto.get_course("BTC"),
        eth=crypto.get_course("ETH"),
        sol=crypto.get_course("SOL"),
        binance=hlink("binance", "https://www.binance.com")
    )
    await call.message.answer(text, reply_markup=keybord_settings_back, disable_web_page_preview=True)


@dp.callback_query_handler(text="volute")
async def volute(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()

    currency = await commands.get_currency(id=call.message.chat.id)
    text = _(
        '💵 Валюта\n\n'
        'Выберите валюту. Этот фильтр влияет на просмотр и создание объявлений.\n\n'
        'Сейчас используется «{currency}».'

    ).format(
        currency=currency
    )
    await call.message.answer(text, reply_markup=keybord_currency)


@dp.callback_query_handler(set_volute.filter(text_name="set_volute"))
async def set_volute(call: CallbackQuery, callback_data: dict):
    currency = callback_data.get("volute")
    await commands.update_currency(id=call.message.chat.id, volute=currency)
    await volute(call)


@dp.callback_query_handler(text="language")
async def language(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
    if user.language == "ru":
        language = '🇷🇺'
    else:
        language = '🇬🇧'
    text = _(
        '🌎 Язык\n\n'
        'Выберите язык интерфейса. Смена языка не повлияет на отправленные ранее сообщения.\n\n'
        'Сейчас используется «{language}».'

    ).format(
        language=language
    )
    await call.message.answer(text, reply_markup=keybord_language)


@dp.callback_query_handler(set_language.filter(text_name="set_language"))
async def set_language(call: CallbackQuery, callback_data: dict):
    currency = callback_data.get("language")
    await commands.update_language(id=call.message.chat.id, volute=currency)
    await language(call)
