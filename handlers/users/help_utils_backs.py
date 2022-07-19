from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp
from keyboards.inline import renew_keyboard
from loader import dp
from states.utils import Hard
from utils.db import Database
from aiogram.dispatcher.filters import Text
from keyboards.default import main_menu, training_weeks_keyboard, program_choice_keyboard
from states import Back, Calculator

database = Database()


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message, state: FSMContext):
    if database.check_subscription(message.from_user.id):
        text = ("Список команд: ",
                "/start - Start a dialog",
                "/help - Show help menu",
                "/time - Show time of sub")

        await message.answer("\n".join(text))
    else:
        await message.answer('Your subscription has expired!', reply_markup=renew_keyboard)
        await state.set_state('renew_sub')

    database.message_counter(message.from_user.id)


# Backs
@dp.message_handler(Text(equals='⬅Back'), state=[Back.P1, Back.P2])
async def second_back(message: types.Message):
    await message.answer("Coming back", reply_markup=program_choice_keyboard)
    await Back.Q0.set()


@dp.message_handler(Text(equals='⬅Back'), state=[Hard.P1_W1, Hard.P1_W2, Hard.P1_W3, Hard.P1_W4])
async def training_p1_back(message: types.Message):
    await message.answer("Coming back", reply_markup=training_weeks_keyboard)
    await Back.P1.set()


@dp.message_handler(Text(equals='⬅Back'), state=[Hard.P2_W1, Hard.P2_W2, Hard.P2_W3, Hard.P2_W4])
async def training_p2_back(message: types.Message):
    await message.answer("Coming back", reply_markup=training_weeks_keyboard)
    await Back.P2.set()


@dp.message_handler(Text(equals='⬅Back'), state=Back.Q2)
async def third_back(message: types.Message, state: FSMContext):
    await message.answer("Coming back", reply_markup=main_menu)
    await state.finish()


@dp.message_handler(Text(equals='⬅Back'), state=[Calculator.SendChoice, Calculator.SendBoo])
async def calculator_back(message: types.Message, state: FSMContext):
    await message.answer("Coming back", reply_markup=main_menu)
    await state.finish()


@dp.message_handler(Text(equals='⬅Back'), state=[Back.Q0, None])
async def first_back(message: types.Message, state: FSMContext):
    await message.answer("Coming back", reply_markup=main_menu)
    await state.finish()


    