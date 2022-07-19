from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentTypes

from keyboards.inline import renew_keyboard
from loader import dp
from utils.db import Database

database = Database()


# Handler to catch expired subs from menu

@dp.message_handler(content_types=ContentTypes.ANY, state=['renew_sub'])
async def renew_sub_func(message: types.Message):
    await message.answer('Renew your subscription!', reply_markup=renew_keyboard)
    database.message_counter(message.from_user.id)


@dp.callback_query_handler(text='Renew', state=['renew_sub'])
async def renew_callback(call: CallbackQuery, state: FSMContext):
    await call.answer('Renewing..')
    # If payment was success -> database.renew() ->
    database.renew_subscription(call.from_user.id)
    # Placeholder
    #
    # If payment was success -> database.renew() ->
    await call.message.answer('Your subscription has been renewed!')
    await state.finish()


# Команда для расчета времени подписки
@dp.message_handler(commands=['time'], state=[None])
async def check_sub_time(message: types.Message):
    await message.answer(f'До конца подписки осталось: {database.sub_time(message.from_user.id)} дней')

