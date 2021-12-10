from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import set_callback
from keyboards.inline.exchange import keybord_exchange, keyboard_shopping, keybord_back_area
from loader import dp
from aiogram.dispatcher import FSMContext

from utils.misc.binance import StockExchange
from utils.db_api import quick_commands as commands

crypto = StockExchange()


@dp.message_handler(text="🔁 Обмен")
async def show_menu_exchange(message: types.Message, state: FSMContext):
    await message.answer("Выберете валюту которую хотите купить/продать", reply_markup=keybord_exchange)

    # await message.answer(f"Биткоин {crypto.get_address('BTC')}")
    # await message.answer(f"Эфир {crypto.get_address('ETH')}")
    # await message.answer(f"Солана {crypto.get_address('SOL')}")
    # await message.answer(f"Текущий курс: 1 BTC = {crypto.get_course('BTC')}.0 RUB")
    # await message.answer(f"Текущий курс: 1 ETH = {crypto.get_course('ETH')}.0 RUB")
    # await message.answer(f"Текущий курс: 1 SOL = {crypto.get_course('SOL')}.0 RUB")
    # await message.answer("Текущий источник: https://www.binance.com", disable_web_page_preview=True)


@dp.callback_query_handler(set_callback.filter(text_name="exchange"))
async def show_set_exchange(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
    print(user)
    currency = callback_data.get("purse")
    if currency == "BTC":
        if user.btc:
            await answer(call, currency)
        else:
            await answer_eror(call, currency)
    elif currency == "ETH":
        if user.eth:
            await answer(call, currency)
        else:
            await answer_eror(call, currency)
    elif currency == "SOL":
        if user.sol:
            await answer(call, currency)
        else:
            await answer_eror(call, currency)

    # await state.update_data(currency=currency)
    # await state.set_state("ask")
    # await call.message.answer(f"Введите номер кошелька  {currency}")


async def answer(call: CallbackQuery, currency):
    await call.message.answer(f'Курс: 1 {currency} = {crypto.get_course(currency)}.0 RUB',
                              reply_markup=keyboard_shopping(currency))


async def answer_eror(call: CallbackQuery, currency):
    await call.message.answer(f'Укажите номер своего кошелька {currency} в личном кабинете',
                              reply_markup=keybord_back_area)


@dp.callback_query_handler(text="backmenuexchange")
async def back_menu_exchange(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer("Выберете валюту которую хотите купить/продать", reply_markup=keybord_exchange)
