from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🔐 Личные данные"),
            KeyboardButton(text="🔁 Обмен")

        ],
        [
            KeyboardButton(text="💎 О сервисе"),
            KeyboardButton(text="🛠 Настройки"),
        ],

    ],
    resize_keyboard=True
)
