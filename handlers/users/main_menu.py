from aiogram import types

from keyboards.default.main_menu import main_menu
from loader import dp, _
from aiogram.dispatcher import FSMContext


@dp.message_handler(text="✅ Полностью согласен")
async def show_menu(message: types.Message):
    await message.answer(_("Выберете категорию которая вам нужна ниже:"), reply_markup=main_menu)


@dp.message_handler(text="✅ I completely agree")
async def show_menu_en(message: types.Message):
    await show_menu(message)


@dp.message_handler(text="Назад", state="backmenu")
async def show_back_menu(message: types.Message, state: FSMContext):
    await message.answer(_("Выберете категорию которая вам нужна ниже:"), reply_markup=main_menu)
    await state.finish()
