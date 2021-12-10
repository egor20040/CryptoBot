from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink, hcode

from data import config
from keyboards.inline.callback_datas import set_callback, set_byi_sell, set_paid
from keyboards.inline.exchange import keybord_exchange, keyboard_shopping, keybord_back_area, keyboard_aplly_bying, \
    paid_keyboard
from loader import dp
from aiogram.dispatcher import FSMContext

from utils.misc.binance import StockExchange
from utils.db_api import quick_commands as commands
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney

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


@dp.callback_query_handler(text="backmenuexchange", state="paid")
async def back_menu_paid(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer("Выберете валюту которую хотите купить/продать", reply_markup=keybord_exchange)
    await state.finish()


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


async def buy_currency_show(call: CallbackQuery, currency, minsumm, wallet, is_sell, maxsum):
    if is_sell:
        await call.message.answer(f"Ввдите сумму в {currency} которую хотите продать\n"
                                  f"\n"
                                  f"Минимальная сумма продажи: {round(minsumm, 6)}"
                                  f"\n"
                                  f"Максимальная сумма продажи: \n"
                                  f"\n"
                                  f"Ваш кошлек для зачисления QIWI: {wallet}")
    else:
        await call.message.answer(f"Ввдите сумму в {currency} которую хотите приобрести\n"
                                  f"\n"
                                  f"Минимальная сумма покупки: {round(minsumm, 6)}"
                                  f"\n"
                                  f"Максимальная сумма покупки: {round(maxsum, 6)}\n"
                                  f"\n"
                                  f"Ваш кошлек для зачисления {currency}: {wallet}")


@dp.callback_query_handler(set_callback.filter(text_name="sell"))
async def sell_currency(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
    currency = callback_data.get("purse")
    minsumm = 1500 / crypto.get_course(currency)
    is_sell = True
    if user.qiwi:
        await buy_currency_show(call, currency, minsumm, user.qiwi, is_sell)
        await state.update_data(currency=currency)
        await state.update_data(minsumm=round(minsumm, 6))
        await state.set_state('sell')
    else:
        await answer_eror(call, currency)


@dp.message_handler(state='sell')
async def buying_currency(message: types.Message, state: FSMContext):
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
            await state.set_state('selling')
        else:
            summ = crypto.get_course(currency) * float(message.text)
            await message.answer(f"Вы получите {round(summ)}.0 RUB на ваш QIWI кошелек"
                                 f"\n"
                                 f"Хотите продолжить?",
                                 reply_markup=keyboard_aplly_bying(round(summ), operation=operation))
            await state.finish()
            await state.set_state('sell')
    except:
        await message.answer(f"Вы ввели некоректную сумму."
                             f"\n"
                             f"Пример правильной суммы: {minsumm}")


@dp.callback_query_handler(set_byi_sell.filter(text_name="final"))
async def show_payment(call: CallbackQuery, callback_data: dict, state: FSMContext):
    summ = callback_data.get("purse")
    operation = callback_data.get("operation")
    payment = Payment(amount=summ)
    payment.create()
    if operation == "buy":
        await call.message.answer(
            "\n".join(
                [
                    f"Оплатите не менее {summ} руб по номеру телефона или по адресу",
                    "",
                    f"Ссылка: {hlink(config.WALLET_QIWI, url=payment.invoice)}",
                    "",
                    "‼️ И обязательно укажите ID платежа:",
                    hcode(payment.id)
                ]
            ),
            reply_markup=paid_keyboard()
        )
        await state.set_state("paid")
        await state.update_data(payment=payment)


@dp.callback_query_handler(set_paid.filter(text_name="paid"), state="paid")
async def show_paid(call: CallbackQuery, callback_data: dict, state: FSMContext):
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
