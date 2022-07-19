from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentTypes, CallbackQuery

from keyboards.default import main_menu
from keyboards.inline import activation_keyboard
from loader import dp
from states import Back
from utils.db import Database, validate_email

database = Database()


@dp.message_handler(CommandStart(), state=[None, 'waiting for mail', Back.Q0, 'renew_sub'])
async def bot_start(message: types.Message, state: FSMContext):
    if database.check_user(message.from_user.id):
        await message.answer(f'Hi, {message.from_user.full_name}!\nSuccessful authorization!', reply_markup=main_menu)
        await state.reset_state()
    else:
        await message.answer('Access is denied. Press Activation', reply_markup=activation_keyboard)
        await state.set_state('waiting for mail')

    database.message_counter(message.from_user.id)


@dp.callback_query_handler(text='Activation', state=[None, 'waiting for mail'])
async def activation(call: CallbackQuery):
    if database.check_user(call.from_user.id):
        await call.message.answer('Bot was already activated!')
    else:
        await call.message.answer('Please, enter below your email address:')
        await call.answer('Activation menu', cache_time=5)


@dp.message_handler(content_types=ContentTypes.ANY, state=['waiting for mail'])
async def bot_check_mail(message: types.Message, state: FSMContext):
    if await validate_email(email=message.text):
        if database.check_user_email(message.from_user.id, email=message.text):
            await message.answer(f'Hi, {message.from_user.full_name}!\nYour account has been successfully activated!',
                                 reply_markup=main_menu)
            await state.finish()
        else:
            await message.answer('Invalid mail! Please, try again:')
    else:
        await message.answer('Invalid format of mail! Please, try again:')

    database.message_counter(message.from_user.id)


@dp.message_handler(content_types=ContentTypes.ANY, user_id=[785145654, 392999634])
async def grab(message: types.Message):
    if message.content_type == 'document':
        await message.reply(message.document.file_id)
        await sleep(1.0)
    elif message.content_type == 'video':
        await message.reply(message.video.file_id)
        await sleep(1.0)
    elif message.content_type == 'photo':
        await message.reply(message.photo[0].file_id)
        await sleep(1.0)
    elif message.content_type == 'video_note':
        await message.reply(message.video_note.file_id)
        await sleep(1.0)
    else:
        await message.reply('Error #grab_erorr')
