from aiogram import types
from aiogram.dispatcher.filters import Text

from data import lecture_buttons, lectures_storage, complex_buttons, complex_storage, check_lists_buttons, \
    check_lists_storage
from loader import dp
from states import Back


@dp.message_handler(Text(equals=lecture_buttons), state=Back.Q0)
async def send_lecture(message: types.Message):
    await message.answer_video(lectures_storage[message.text], protect_content=True)


@dp.message_handler(Text(equals=complex_buttons), state=Back.Q0)
async def send_complex(message: types.Message):
    if message.text not in ('Warm-up ', 'Press No. 1', 'Press No. 2'):
        await message.answer_video(complex_storage[message.text],
                                   caption='Each exercise is repeated 10-15 times on each side.',
                                   protect_content=True)
    else:
        await message.answer_video(complex_storage[message.text])


@dp.message_handler(Text(equals=check_lists_buttons), state=Back.Q0)
async def send_check_list(message: types.Message):
    await message.answer_document(check_lists_storage[message.text], protect_content=True)


