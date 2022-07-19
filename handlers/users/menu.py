from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data import main_menu_buttons
from keyboards.default import complex_keyboard, lectures, check_lists_keyboard
from keyboards.inline import activation_keyboard, renew_keyboard
from loader import dp
from states import Back, Calculator
from utils.db import Database

database = Database()


@dp.message_handler(Text(equals=main_menu_buttons))
async def get_text(message: types.Message, state: FSMContext):
    if database.check_user(message.from_user.id):
        if database.check_subscription(message.from_user.id):

            if message.text == 'Lectures':
                await message.answer('Opening lectures..', reply_markup=lectures)
                await Back.Q0.set()

            elif message.text == 'Checklists':
                await message.answer('Opening checklists', reply_markup=check_lists_keyboard)

            elif message.text == 'Complexes':
                await message.answer('Opening complexes..', reply_markup=complex_keyboard)
                await Back.Q0.set()

            elif message.text == 'Calories Calculator':
                await message.answer('Welcome to calculator!\n'
                                     'To start the calculation send your weight in kg:')
                await Calculator.SendWeight.set()

        else:
            await message.answer('Your subscription has expired!', reply_markup=renew_keyboard)
            await state.set_state('renew_sub')

    else:
        await message.answer("🚫Access is denied!\n\nTo activate press 'Activate'.\n If you have troubles with "
                             "activation, please contact us by support button below.",
                             reply_markup=activation_keyboard)