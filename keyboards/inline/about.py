from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keybord_about = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text="💎 Наш канал",
                                                 url="https://t.me/sliv_litvinwb"

                                             ),
                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text="💬 Поддержка",
                                                 url="https://t.me/rtiandi"

                                             ),

                                         ],
                                         [
                                             InlineKeyboardButton(
                                                 text="🗣 Реферальная система",
                                                 callback_data="referal"

                                             ),

                                         ]

                                     ]
                                     )
keybord_back_about = InlineKeyboardMarkup(row_width=1,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(
                                                      text="⬅️ Назад",
                                                      callback_data="backreferal"

                                                  ),
                                              ]
                                          ]
                                          )
