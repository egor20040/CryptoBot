from aiogram.utils.callback_data import CallbackData

set_callback = CallbackData("set", "text_name", "purse")
set_byi_sell = CallbackData("set", "text_name", "operation", "purse")
set_paid = CallbackData("set", "text_name")  # оплата платежа
set_volute = CallbackData("set", "text_name", "volute")  # изменение волюты
set_language = CallbackData("set", "text_name", "language")  # изменение языка
