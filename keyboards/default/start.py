from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _
start = ReplyKeyboardMarkup(
    [

        [
            KeyboardButton(
                text=_("✅ Полностью согласен")
                       ),

        ]

    ],
    resize_keyboard=True
)
