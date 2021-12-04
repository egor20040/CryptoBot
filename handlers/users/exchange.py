from aiogram import types

from loader import dp
from aiogram.dispatcher import FSMContext

from utils.misc.binance import get_address_btc, get_address_eth, get_address_sol


@dp.message_handler(text="🔁 Обмен")
async def show_menu(message: types.Message, state: FSMContext):
    await message.answer(f"Биткоин {get_address_btc()}")
    await message.answer(f"Эфир {get_address_eth()}")
    await message.answer(f"Солана {get_address_sol()}")
    await state.finish()