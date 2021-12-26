from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.exchange.exchange import buy_currency_show
from keyboards.inline.callback_datas import set_callback, set_paid
from keyboards.inline.exchange import keyboard_aplly_bying, paid_keyboard, keybord_exchange
from loader import dp
from utils.misc.binance import StockExchange
from utils.db_api import quick_commands as commands
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney

crypto = StockExchange()


@dp.callback_query_handler(set_callback.filter(text_name="buy"))
async def buy_currency(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
    currency = callback_data.get("purse")
    minsumm = 1500 / crypto.get_course(currency)
    maxsum = 1000000 / crypto.get_course(currency)
    is_sell = False
    if 'BTC' == currency:
        await buy_currency_show(call, currency, minsumm, user.btc, is_sell, maxsum)
    if 'ETH' == currency:
        await buy_currency_show(call, currency, minsumm, user.eth, is_sell, maxsum)
    if 'SOL' == currency:
        await buy_currency_show(call, currency, minsumm, user.sol, is_sell, maxsum)

    await state.update_data(currency=currency)
    await state.update_data(minsumm=round(minsumm, 6))
    await state.update_data(maxsum=round(maxsum, 6))
    await state.set_state('bying')


@dp.message_handler(state='bying')
async def buying_currency(message: types.Message, state: FSMContext):
    data = await state.get_data()
    currency = data.get("currency")
    minsumm = data.get("minsumm")
    maxsum = data.get("maxsum")
    operation = "buy"
    try:
        if minsumm > float(message.text):
            await message.answer(f"Минимальная сумма для покупки {minsumm}\n"
                                 f"\n"
                                 f"Ввдеите корректную сумму\n"
                                 f"\n"
                                 )
            await state.set_state('bying')
        elif maxsum < float(message.text):
            await message.answer(f"Максимальная сумма для покупки {maxsum}\n"
                                 f"\n"
                                 f"Ввдеите корректную сумму\n"
                                 f"\n"
                                 )
            await state.set_state('bying')
        else:
            summ = crypto.get_course(currency) * float(message.text)
            await message.answer(f"Для оплаты нужно {round(summ)}.0 RUB"
                                 f"\n"
                                 f"Хотите продолжить?", reply_markup=keyboard_aplly_bying(round(summ), operation))
            await state.finish()
    except:
        await message.answer(f"Вы ввели некоректную сумму."
                             f"\n"
                             f"Пример правильной суммы: {minsumm}")


@dp.callback_query_handler(set_paid.filter(text_name="paid"), state="paid")
async def show_paid(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена", reply_markup=paid_keyboard())

    except NotEnoughMoney:
        await call.message.answer("Не хватает денег", reply_markup=paid_keyboard())

    else:
        await call.message.answer(f"Оплата прошла успешно"
                                  f"\n"
                                  f"Валюта на ваш кошелек будет зачислена в тетечении 15 минут",
                                  reply_markup=keybord_exchange)
        await state.finish()
