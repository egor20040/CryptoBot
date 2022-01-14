from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import set_callback, set_byi_sell, set_paid
from loader import _

keybord_exchange = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="SOl",
                                                    callback_data=set_callback.new(text_name="exchange", purse="SOL")

                                                ),
                                                InlineKeyboardButton(
                                                    text="BTC",
                                                    callback_data=set_callback.new(text_name="exchange", purse="BTC")

                                                ),

                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="ETH",
                                                    callback_data=set_callback.new(text_name="exchange", purse="ETH")

                                                ),

                                            ]

                                        ]
                                        )


def keyboard_add_currency(currency):
    text = _("Добавить {currency} кошелек").format(
        currency=currency
    )
    keybord_back_area = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=text,
                                                         callback_data=set_callback.new(text_name="purse",
                                                                                        purse=currency)

                                                     ),

                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text=_("⬅️ Назад"),
                                                         callback_data="backmenuexchange"

                                                     ),

                                                 ]

                                             ]
                                             )
    return keybord_back_area


def keyboard_shopping(currency):
    keybord_shopping = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=_("📈 Купить"),
                                                        callback_data=set_callback.new(text_name="buy", purse=currency)

                                                    ),
                                                    InlineKeyboardButton(
                                                        text=_("📉 Продать"),
                                                        callback_data=set_callback.new(text_name="sell", purse=currency)

                                                    ),

                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text=_("⬅️ Назад"),
                                                        callback_data="backmenuexchange"

                                                    ),

                                                ]

                                            ]
                                            )
    return keybord_shopping


def keyboard_aplly_bying(summ, operation):
    keybord_bying = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(
                                                     text=_("Продолжить"),
                                                     callback_data=set_byi_sell.new(text_name="final",
                                                                                    operation=operation, purse=summ)

                                                 ),

                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text=_("⬅️ Назад"),
                                                     callback_data="backmenuexchange"

                                                 ),

                                             ]

                                         ]
                                         )
    return keybord_bying


def paid_keyboard(url):
    paid_keyboard = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(
                                                     text=_("Перейти к оплате по ссылке"),
                                                     url=url

                                                 ),

                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text=_("✅ Проверить пополнение ✅"),
                                                     callback_data=set_paid.new(text_name="paid")

                                                 ),

                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text=_("❌ Отменить пополнение ❌"),
                                                     callback_data="backmenuexchange"

                                                 ),

                                             ]

                                         ]
                                         )
    return paid_keyboard
