from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink, hcode

from data import config
from keyboards.inline.callback_datas import set_callback, set_byi_sell
from keyboards.inline.exchange import keybord_exchange, keyboard_shopping,  \
    paid_keyboard, keyboard_add_currency
from loader import dp
from aiogram.dispatcher import FSMContext

from utils.misc.binance import StockExchange
from utils.db_api import quick_commands as commands
from utils.misc.qiwi import Payment

crypto = StockExchange()


@dp.message_handler(text="🔁 Обмен")
async def show_menu_exchange(message: types.Message):
    await message.answer("🔁 Обмен \n\n Выберете валюту которую хотите купить/продать", reply_markup=keybord_exchange)


@dp.callback_query_handler(set_callback.filter(text_name="exchange"))
async def show_set_exchange(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.delete()
    user = await commands.select_user(call.message.chat.id)
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


async def answer(call: CallbackQuery, currency):
    await call.message.answer(f'Курс: 1 {currency} = {crypto.get_course(currency)}.0 RUB',
                              reply_markup=keyboard_shopping(currency))


async def answer_eror(call: CallbackQuery, currency):
    await call.message.answer(f'Укажите номер своего кошелька {currency} в личном кабинете',
                              reply_markup=keyboard_add_currency(currency))


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


async def buy_currency_show(call: CallbackQuery, currency, minsumm, wallet, is_sell, maxsum):
    if is_sell:
        await call.message.answer(f"Ввдите сумму в {currency} которую хотите продать\n"
                                  f"\n"
                                  f"Минимальная сумма продажи: {round(minsumm, 6)}"
                                  f"\n"
                                  f"Максимальная сумма продажи: {round(maxsum, 6)}\n"
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


@dp.callback_query_handler(set_byi_sell.filter(text_name="final"))
async def show_payment(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    summ = callback_data.get("purse")
    operation = callback_data.get("operation")
    if operation == "buy":
        payment = Payment(amount=summ)
        payment.create()
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
    else:
        data = await state.get_data()
        currency = data.get("currency")
        await call.message.answer(
            "\n".join(
                [
                    f"Оплатите не менее {summ} {currency} по номеру счета:",
                    "",
                    f"{crypto.get_address(currency)}",
                    "",
                ]
            ),
            reply_markup=paid_keyboard()
        )
        await state.set_state("paidcrypto")
