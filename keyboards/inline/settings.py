from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keybord_settings = InlineKeyboardMarkup(row_width=2,
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
