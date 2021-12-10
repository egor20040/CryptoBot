from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import set_callback

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

keybord_back_area = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="⬅️ Назад",
                                                    callback_data="backmenuexchange"

                                                ),

                                            ]

                                        ]
                                        )



def keyboard_shopping(currency):
    keybord_shopping = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text="Купить",
                                                        callback_data=set_callback.new(text_name="buy", purse=currency)

                                                    ),
                                                    InlineKeyboardButton(
                                                        text="Продать",
                                                        callback_data=set_callback.new(text_name="sell", purse=currency)

                                                    ),

                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text="Назад",
                                                        callback_data="backmenuexchange"

                                                    ),

                                                ]

                                            ]
                                            )
    return keybord_shopping
