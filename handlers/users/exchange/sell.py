from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.exchange.exchange import buy_currency_show, answer_eror
from keyboards.inline.callback_datas import set_callback, set_paid
from keyboards.inline.exchange import keyboard_aplly_bying, keybord_exchange
from utils.misc.binance import StockExchange
from utils.db_api import quick_commands as commands
from loader import dp

crypto = StockExchange()


@dp.callback_query_handler(set_callback.filter(text_name="sell"))
async def sell_currency(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
    currency = callback_data.get("purse")
    minsumm = 1500 / crypto.get_course(currency)
    maxsum = 600000 / crypto.get_course(currency)
    is_sell = True
    if user.qiwi:
        await buy_currency_show(call, currency, minsumm, user.qiwi, is_sell, maxsum)
        await state.update_data(currency=currency)
        await state.update_data(minsumm=round(minsumm, 6))
        await state.set_state('sell')
    else:
        await answer_eror(call, currency)


@dp.message_handler(state='sell')
async def selling_currency(message: types.Message, state: FSMContext):
    data = await state.get_data()
    currency = data.get("currency")
    minsumm = data.get("minsumm")
    operation = "sell"
    try:
        if minsumm > float(message.text):
            await message.answer(f"Минимальная сумма для продажи: {minsumm}\n"
                                 f"\n"
                                 f"Ввдеите корректную сумму\n"
                                 f"\n"
                                 )
            await state.set_state('sell')
        else:
            summ = crypto.get_course(currency) * float(message.text)
            await message.answer(f"Вы получите {round(summ)}.0 RUB на ваш QIWI кошелек"
                                 f"\n"
                                 f"Хотите продолжить?",
                                 reply_markup=keyboard_aplly_bying(summ=message.text, operation=operation))
            await state.finish()
            await state.update_data(currency=currency)
    except:
        await message.answer(f"Вы ввели некоректную сумму."
                             f"\n"
                             f"Пример правильной суммы: {minsumm}")


@dp.callback_query_handler(set_paid.filter(text_name="paid"), state="paidcrypto")
async def show_paid(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(f"Идет проверка оплаты...."
                              f"\n"
                              f"Если оплата прошла успешно, на ваш будут зачислены средства."
                              f"В случае ошибки оплаты мы вам сообщим",
                              reply_markup=keybord_exchange)
    await state.finish()
