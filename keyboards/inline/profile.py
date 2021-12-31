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

                                           ]

                                       ]
                                       )

