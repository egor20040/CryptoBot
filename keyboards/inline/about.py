from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _

keybord_about = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text=_("💎 Наш канал"),
                                                 url="https://t.me/crypto_market_invest"

                                             ),
                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text=_("💬 Поддержка"),
                                                 url="https://t.me/rtiandi"

                                             ),

                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text=_("🗣 Реферальная система"),
                                                 callback_data="referal"

                                             ),

                                         ]

                                     ]
                                     )
keybord_back_about = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(
                                                      text=_("⬅️ Назад"),
                                                      callback_data="backreferal"

                                                  ),
                                              ]
                                          ]
                                          )
