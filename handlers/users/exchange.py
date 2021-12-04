from aiogram import types

from loader import dp
from aiogram.dispatcher import FSMContext

from utils.misc.binance import StockExchange


@dp.message_handler(text="🔁 Обмен")
async def show_menu(message: types.Message, state: FSMContext):
    crypto = StockExchange()
    await message.answer(f"Биткоин {crypto.get_address('BTC')}")
    await message.answer(f"Эфир {crypto.get_address('ETH')}")
    await message.answer(f"Солана {crypto.get_address('SOL')}")
    await message.answer(f"Текущий курс: 1 BTC = {crypto.get_course('BTC')}.0 RUB")
    await message.answer(f"Текущий курс: 1 ETH = {crypto.get_course('ETH')}.0 RUB")
    await message.answer(f"Текущий курс: 1 SOL = {crypto.get_course('SOL')}.0 RUB")
    await message.answer("Текущий источник: https://www.binance.com", disable_web_page_preview=True)
    await state.finish()
