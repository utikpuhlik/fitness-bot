from asyncio import sleep
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from states import Mailing
from utils.db import Database

database = Database()


@dp.message_handler(user_id=[785145654, 392999634], commands=["all"])
async def mailing(message: types.Message):
    await message.answer('Text of your message:')
    await message.answer("*To leave mailing, enter: 'exit'")
    await Mailing.Text.set()


@dp.message_handler(state=Mailing.Text)
async def mailing(message: types.Message, state: FSMContext):
    text = message.text
    if text == 'exit':
        await message.answer(f'You left the mailing state')
    else:
        count_of_users = 0
        for user in database.get_all_users():
            user = user[0]
            try:
                if user in (896114308, 785145654, 621767121):
                    pass
                else:
                    await bot.send_message(chat_id=user, text=text)
                    await sleep(0.3)
                    count_of_users += 1
            except Exception:
                pass

        await message.answer(f'Mailing was success, message was sent to {count_of_users} users')
    await state.finish()
