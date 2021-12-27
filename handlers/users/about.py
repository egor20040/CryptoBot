from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink

from keyboards.inline.about import keybord_about, keybord_back_about
from loader import dp


@dp.message_handler(text="🚀 О сервисе Crypto Market")
async def show_menu(message: types.Message):
    text = [
        '🚀 О сервисе Crypto Market',
        '',
        'Crypto Market, это место где ты можешь купить или продать криптоволюту с минимальной комиссией.',
        '',
        'Сервис не хранит криптоволюту , а выступает обменником между биржей и пользователем.',
        '',
        'Мы зарабатываем на комисии и берем 0.45% от сделки.У нас так же есть реферальная система ознакомится с ней можно по кнопке ниже ⬇️',
        '',
        f'Так же всем кто интересуется миром криптоволюты , советуем наш телеграмм {hlink("канал", url="https://t.me/sliv_litvinwb")}. Там мы публикуем новости и выгодные инвестиции.',

    ]
    await message.answer('\n'.join(text), reply_markup=keybord_about, disable_web_page_preview=True)


@dp.callback_query_handler(text="backreferal")
async def show_set_menu(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    text = [
        '🚀 О сервисе Crypto Market',
        '',
        'Crypto Market, это место где ты можешь купить или продать криптоволюту с минимальной комиссией.',
        '',
        'Сервис не хранит криптоволюту , а выступает обменником между биржей и пользователем.',
        '',
        'Мы зарабатываем на комисии и берем 0.45% от сделки.У нас так же есть реферальная система ознакомится с ней можно по кнопке ниже ⬇️',
        '',
        f'Так же всем кто интересуется миром криптоволюты , советуем наш телеграмм {hlink("канал", url="https://t.me/sliv_litvinwb")}. Там мы публикуем новости и выгодные инвестиции.',

    ]
    await call.message.answer('\n'.join(text), reply_markup=keybord_about, disable_web_page_preview=True)


@dp.callback_query_handler(text="referal")
async def show_set_menu(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    bot_user = await dp.bot.get_me()
    text = [
        '🗣 Реферальная система',
        '',
        'За каждого приглашенного пользователя мы выплачиваем 0.15% от общей суммы его сделок.',
        '',
        f'Ваша реферальная ссылка: http://t.me/{bot_user.username}?start={call.message.from_user.id}',
        '',
        'Для того чтобы получить реферальные средства перейдите в \n«🔐 Личные данные»',
        '',

    ]
    await call.message.answer('\n'.join(text), reply_markup=keybord_back_about, disable_web_page_preview=True)
