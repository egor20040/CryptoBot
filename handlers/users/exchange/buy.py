from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from handlers.users.exchange.exchange import buy_currency_show
from keyboards.inline.callback_datas import set_callback, set_paid
from keyboards.inline.exchange import keyboard_aplly_bying, paid_keyboard, keybord_exchange
from loader import dp, _
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
            text = _(
                "Минимальная сумма для покупки {minsumm}\n"
                "\n"
                "Ввдеите корректную сумму\n"
                "\n"
            ).format(
                minsumm=minsumm
            )
            await message.answer(text)
            await state.set_state('bying')
        elif maxsum < float(message.text):
            text = _(
                "Максимальная сумма для покупки {maxsum}\n"
                "\n"
                "Ввдеите корректную сумму\n"
            ).format(
                maxsum=maxsum
            )
            await message.answer(text)
            await state.set_state('bying')
        else:
            summ = crypto.get_course(currency) * float(message.text)
            text = _(
                "Для оплаты нужно {sum}.0 RUB\n"
                "\n"
                "Хотите продолжить?\n"
            ).format(
                sum=round(summ)
            )
            await message.answer(text, reply_markup=keyboard_aplly_bying(round(summ), operation))
            await state.finish()
    except:
        text = _(
            "Вы ввели некоректную сумму.\n"
            "\n"
            "Пример правильной суммы: {minsumm}\n"
        ).format(
            minsumm=minsumm
        )
        await message.answer(text)


@dp.callback_query_handler(set_paid.filter(text_name="paid"), state="paid")
async def show_paid(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    payment: Payment = data.get("payment")
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer(_("Транзакция не найдена"), reply_markup=paid_keyboard())

    except NotEnoughMoney:
        await call.message.answer(_("Не хватает денег"), reply_markup=paid_keyboard())

    else:
        text = _(
            "Оплата прошла успешно.\n"
            "\n"
            "Валюта на ваш кошелек будет зачислена в тетечении 15 минут\n"
        )
        await call.message.answer(text, reply_markup=keybord_exchange)
        await state.finish()
