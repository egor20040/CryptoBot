from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import set_volute, set_language
from loader import _

keybord_course = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text=_("🌎 Язык"),
                                                  callback_data="language"

                                              ),
                                              InlineKeyboardButton(
                                                  text=_("📊 Курс"),
                                                  callback_data="course"

                                              ),

                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text=_("💵 Выбрать валюту"),
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
                                                    callback_data=set_volute.new(text_name="set_volute", volute="RUB")

                                                ),
                                                InlineKeyboardButton(
                                                    text="USD",
                                                    callback_data=set_volute.new(text_name="set_volute", volute="USD")

                                                ),
                                                InlineKeyboardButton(
                                                    text="EUR",
                                                    callback_data=set_volute.new(text_name="set_volute", volute="EUR")

                                                ),

                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text=_("⬅️ Назад"),
                                                    callback_data="backsettings"

                                                ),

                                            ]

                                        ]
                                        )

keybord_settings_back = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=_("⬅️ Назад"),
                                                         callback_data="backsettings"

                                                     ),

                                                 ],

                                             ]
                                             )
keybord_language = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="🇷🇺",
                                                    callback_data=set_language.new(text_name="set_language",
                                                                                   language="ru")

                                                ),
                                                InlineKeyboardButton(
                                                    text="🇬🇧",
                                                    callback_data=set_language.new(text_name="set_language",
                                                                                   language="en")

                                                ),

                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text=_("⬅️ Назад"),
                                                    callback_data="backsettings"

                                                ),

                                            ]

                                        ]
                                        )
