from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import set_callback
from loader import _

keybord_profile = InlineKeyboardMarkup(row_width=2,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(
                                                   text=_("Добавить QIWI"),
                                                   callback_data=set_callback.new(text_name="purse", purse="QIWI")

                                               ),
                                               InlineKeyboardButton(
                                                   text=_("Добавить BTC"),
                                                   callback_data=set_callback.new(text_name="purse", purse="BTC")

                                               ),

                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text=_("Добавить ETH"),
                                                   callback_data=set_callback.new(text_name="purse", purse="ETH")

                                               ),
                                               InlineKeyboardButton(
                                                   text=_("Добавить SOL"),
                                                   callback_data=set_callback.new(text_name="purse", purse="SOL")

                                               ),

                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text=_("⬅️ Назад"),
                                                   callback_data='back_profile'

                                               ),

                                           ]

                                       ]
                                       )

keybord_profile_main = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=_("💵 Добавить Кошелек"),
                                                        callback_data='add_wallet'

                                                    ),
                                                    InlineKeyboardButton(
                                                        text=_("📑 Отчеты"),
                                                        callback_data='reports'

                                                    ),

                                                ],
                                                [
                                                    InlineKeyboardButton(
                                                        text=_("💰 Реферальные накопления"),
                                                        callback_data='referral_savings'

                                                    ),
                                                    InlineKeyboardButton(
                                                        text=_("🎟 Промокоды"),
                                                        callback_data='promo'

                                                    ),

                                                ]

                                            ]
                                            )

keybord_profile_promo = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=_("Активировать"),
                                                         callback_data="activate_promo"

                                                     ),

                                                 ],
                                                 [
                                                     InlineKeyboardButton(
                                                         text=_("⬅️ Назад"),
                                                         callback_data="back_profile"

                                                     ),

                                                 ],

                                             ]
                                             )


keybord_back_profile = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[

                                                 [
                                                     InlineKeyboardButton(
                                                         text=_("⬅️ Назад"),
                                                         callback_data="back_profile"

                                                     ),

                                                 ],

                                             ]
                                             )

