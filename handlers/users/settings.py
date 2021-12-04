from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.settings import keybord_settings, keybord_settings_back
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from utils.misc.binance import StockExchange


@dp.message_handler(text="🛠 Настройки")
async def show_menu(message: types.Message):
    text = [
        '🛠 Настройки',
        '',
        f'Ваш id: {message.from_user.id}',
        '',
        'Что Вы хотите изменить?',
    ]
    await message.answer('\n'.join(text), reply_markup=keybord_settings)


@dp.callback_query_handler(text="backsettings")
async def show_back_menu_settings(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    text = [
        '🛠 Настройки',
        '',
        f'Ваш id: {call.message.from_user.id}',
        '',
        'Что Вы хотите изменить?',
    ]
    await call.message.answer('\n'.join(text), reply_markup=keybord_settings)


@dp.callback_query_handler(text="course")
async def course(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    crypto = StockExchange()
    text = [
        '📊 Курс',
        '',
        'Текущий курс:',
        '',
        f'1 BTC = {crypto.get_course("BTC")}.0 RUB',
        f'1 ETH = {crypto.get_course("ETH")}.0 RUB',
        f'1 SOL = {crypto.get_course("SOL")}.0 RUB',
        '',
        f'Текущий источник: {hlink("binance", "https://www.binance.com")}',
    ]
    await call.message.answer('\n'.join(text), reply_markup=keybord_settings_back, disable_web_page_preview=True)


