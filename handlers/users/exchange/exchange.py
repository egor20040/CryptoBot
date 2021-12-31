from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink, hcode

from data import config
from keyboards.inline.callback_datas import set_callback, set_byi_sell
from keyboards.inline.exchange import keybord_exchange, keyboard_shopping, \
    paid_keyboard, keyboard_add_currency
from loader import dp, _
from aiogram.dispatcher import FSMContext

from utils.misc.binance import StockExchange
from utils.db_api import quick_commands as commands
from utils.misc.qiwi import Payment

crypto = StockExchange()


@dp.message_handler(text="🔁 Exchange")
async def snow_menu_en(message: types.Message):
    await show_menu_exchange(message)


@dp.message_handler(text="🔁 Обмен")
async def show_menu_exchange(message: types.Message):
    await message.answer(_("🔁 Обмен \n\n Выберете валюту которую хотите купить/продать"),
                         reply_markup=keybord_exchange)


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
    text = _(
        'Курс: 1 {currency} = {course}.0 RUB'
    ).format(
        currency=currency,
        course=crypto.get_course(currency)
    )
    await call.message.answer(text, reply_markup=keyboard_shopping(currency))


async def answer_eror(call: CallbackQuery, currency):
    text = _(
        'Укажите номер своего кошелька {currency} в личном кабинете'
    ).format(
        currency=currency,
    )
    await call.message.answer(text, reply_markup=keyboard_add_currency(currency))


@dp.callback_query_handler(text="backmenuexchange")
async def back_menu_exchange(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(_("Выберете валюту которую хотите купить/продать"), reply_markup=keybord_exchange)


@dp.callback_query_handler(text="backmenuexchange", state="paid")
async def back_menu_paid(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer(_("Выберете валюту которую хотите купить/продать"), reply_markup=keybord_exchange)
    await state.finish()


async def buy_currency_show(call: CallbackQuery, currency, minsumm, wallet, is_sell, maxsum):
    if is_sell:
        text = _(
            "Ввдите сумму в {currency} которую хотите продать\n"
            "\n"
            "Минимальная сумма продажи: {minsumm}"
            "\n"
            "Максимальная сумма продажи: {maxsum}\n"
            "\n"
            "Ваш QIWI кошлек для зачисления: {wallet}"
        ).format(
            currency=currency,
            minsumm=round(minsumm, 6),
            maxsum=round(maxsum, 6),
            wallet=wallet
        )
        await call.message.answer(text)
    else:
        text = _(
            "Ввдите сумму в {currency} которую хотите приобрести\n"
            "\n"
            "Минимальная сумма продажи: {minsumm}"
            "\n"
            "Максимальная сумма продажи: {maxsum}\n"
            "\n"
            "Ваш {currency} кошлек для зачисления : {wallet}"
        ).format(
            currency=currency,
            minsumm=round(minsumm, 6),
            maxsum=round(maxsum, 6),
            wallet=wallet
        )
        await call.message.answer(text)


@dp.callback_query_handler(set_byi_sell.filter(text_name="final"))
async def show_payment(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    summ = callback_data.get("purse")
    operation = callback_data.get("operation")
    if operation == "buy":
        payment = Payment(amount=summ)
        payment.create()
        text = _(
            "Оплатите не менее {summ} руб по номеру телефона или по адресу\n"
            "\n"
            "Ссылка: {link}\n"
            "\n"
            "‼️ И обязательно укажите ID платежа: {id}\n"
        ).format(
            summ=summ,
            link=hlink(config.WALLET_QIWI, url=payment.invoice),
            id=hcode(payment.id)
        )
        await call.message.answer(text, reply_markup=paid_keyboard())
        await state.set_state("paid")
        await state.update_data(payment=payment)
    else:
        data = await state.get_data()
        currency = data.get("currency")
        text = _(
            "Оплатите не менее {summ} {currency} по номеру счета:\n"
            "\n"
            "{address}\n"
        ).format(
            summ=summ,
            currency=currency,
            address=crypto.get_address(currency)
        )
        await call.message.answer(text, reply_markup=paid_keyboard())
        await state.set_state("paidcrypto")
