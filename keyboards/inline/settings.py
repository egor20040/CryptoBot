from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keybord_course = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="🌎 Язык",
                                                  callback_data="language"

                                              ),
                                              InlineKeyboardButton(
                                                  text="📊 Курс",
                                                  callback_data="course"

                                              ),

                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="💵 Выбрать валюту",
                                                  callback_data="volute"

                                              ),

                                          ]

                                      ]
                                      )

keybord_currency = InlineKeyboardMarkup(row_width=3,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="RUB",
                                                    callback_data="currency"

                                                ),
                                                InlineKeyboardButton(
                                                    text="USD",
                                                    callback_data="currency"

                                                ),
                                                InlineKeyboardButton(
                                                    text="EUR",
                                                    callback_data="currency"

                                                ),

                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="⬅️ Назад",
                                                    callback_data="backsettings"

                                                ),

                                            ]

                                        ]
                                        )

keybord_settings_back = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text="⬅️ Назад",
                                                         callback_data="backsettings"

                                                     ),

                                                 ],

                                             ]
                                             )
