from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hlink

from keyboards.inline.about import keybord_about, keybord_back_about
from loader import dp, _


@dp.message_handler(text="🚀 About Crypto Market Service")
async def snow_menu_en(message: types.Message):
    await show_menu(message)


@dp.message_handler(text="🚀 О сервисе Crypto Market")
async def show_menu(message: types.Message):
    text = _(
        '🚀 О сервисе Crypto Market\n\n'
        'Crypto Market, это место где ты можешь купить или продать криптоволюту с минимальной комиссией.\n\n'
        'Сервис не хранит криптоволюту , а выступает обменником между биржей и пользователем.\n\n'
        'Мы зарабатываем на комисии и берем 0.45% от сделки.У нас так же есть реферальная система ознакомится с ней можно по кнопке ниже ⬇️\n\n'
        'Так же всем кто интересуется миром криптоволюты , советуем наш телеграмм {сhannel}. Там мы публикуем новости и выгодные инвестиции.'

    ).format(
        сhannel=hlink(_("канал"), url="https://t.me/sliv_litvinwb")
    )
    await message.answer(text, reply_markup=keybord_about, disable_web_page_preview=True)


@dp.callback_query_handler(text="backreferal")
async def show_set_menu(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    text = _(
        '🚀 О сервисе Crypto Market\n\n'
        'Crypto Market, это место где ты можешь купить или продать криптоволюту с минимальной комиссией.\n\n'
        'Сервис не хранит криптоволюту , а выступает обменником между биржей и пользователем.\n\n'
        'Мы зарабатываем на комисии и берем 0.45% от сделки.У нас так же есть реферальная система ознакомится с ней можно по кнопке ниже ⬇️\n\n'
        'Так же всем кто интересуется миром криптоволюты , советуем наш телеграмм {сhannel}. Там мы публикуем новости и выгодные инвестиции.'

    ).format(
        сhannel=hlink(_("канал"), url="https://t.me/sliv_litvinwb")
    )
    await call.message.answer(text, reply_markup=keybord_about, disable_web_page_preview=True)


@dp.callback_query_handler(text="referal")
async def show_set_menu(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete()
    bot_user = await dp.bot.get_me()
    text = _(
        '🗣 Реферальная система\n\n'
        'За каждого приглашенного пользователя мы выплачиваем 0.15% от общей суммы его сделок.\n\n'
        'Ваша реферальная ссылка: http://t.me/{bot_name}?start={user_id}\n\n'
        'Для того чтобы получить реферальные средства перейдите в \n«🔐 Личные данные»'
    ).format(
        bot_name=bot_user.username,
        user_id=call.message.from_user.id
    )
    await call.message.answer(text, reply_markup=keybord_back_about, disable_web_page_preview=True)
