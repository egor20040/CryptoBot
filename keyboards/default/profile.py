from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Добавить BTC кошелек"),
            KeyboardButton(text="Добавить ETH кошелек")

        ],
        [
            KeyboardButton(text="Добавить SOL кошелек"),
            KeyboardButton(text="Добавить QIWI кошелек"),
        ],
        [
            KeyboardButton(text="Назад")
        ]

    ],
    resize_keyboard=True
)
