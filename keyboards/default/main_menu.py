from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=_("🔐 Личные данные")),
            KeyboardButton(text=_("🔁 Обмен"))

        ],
        [
            KeyboardButton(text=_("🚀 О сервисе Crypto Market")),
            KeyboardButton(text=_("🛠 Настройки")
                           ),
        ],

    ],
    resize_keyboard=True
)
