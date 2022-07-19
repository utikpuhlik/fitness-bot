from aiogram import types
from aiogram.dispatcher import FSMContext

from data import activity_types_buttons, activity_types
from keyboards.default import activity_types_keyboard, main_menu, calculator_choice_keyboard
from loader import dp
from states import Calculator


@dp.message_handler(state=Calculator.SendWeight)
async def get_answer_weight(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except Exception as NotValid:
        await message.answer('Invalid input form, please send weight in kg')

    else:
        await state.update_data(
            {
                'weight': float(message.text)
            }
        )
        await Calculator.SendHeight.set()
        await message.answer('Excellent! Now enter your height in cm:')
        # print(list(Calculator.all_states))


@dp.message_handler(state=Calculator.SendHeight)
async def get_answer_height(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except Exception as NotValid:
        await message.answer('Invalid input form, please send height in cm')

    else:
        await state.update_data(
            {
                'height': float(message.text)
            }
        )
        await Calculator.SendAge.set()
        await message.answer('Excellent! Now enter your age:')


@dp.message_handler(state=Calculator.SendAge)
async def get_answer_age(message: types.Message, state: FSMContext):
    try:
        float(message.text)
    except Exception as NotValid:
        await message.answer('Invalid input form, please send an integer')

    else:
        await state.update_data(
            {
                'age': float(message.text)
            }
        )
        mid_res = await state.get_data()
        boo = mid_res['weight'] * 10 + mid_res['height'] * 6.25 - mid_res['age'] * 5 - 161
        await state.update_data(
            {
                "boo": boo
            }
        )
        await message.answer(f'This is your basal metabolism - {boo} calories. You cannot go below this calorie content.')
        await message.answer('Now, choose your activity type from the options below:',
                             reply_markup=activity_types_keyboard)
        await Calculator.SendBoo.set()


@dp.message_handler(state=Calculator.SendBoo)
async def get_answer_boo(message: types.Message, state: FSMContext):
    if message.text in activity_types_buttons:
        await state.update_data(
            {
                'boo_type': activity_types[message.text]
            }
        )
        result = await state.get_data()
        result = result['boo_type'] * result['boo']
        await state.update_data(
            {
                'norm': round(result),
                'proteins': round(0.3 * result / 4),
                'fat': round(0.25 * result / 9),
                'carbohydrates': round(0.45 * result / 4)
            }
        )
        result = await state.get_data()
        await message.answer(f"Your calorie intake: {result['norm']}", reply_markup=calculator_choice_keyboard)
        await message.answer(f"If your goal is not to lose weight or gain weight, then this is the number of calories that "
                             f"you need to eat a day to maintain weight.\n\nPFC:\n"
                             f"Proteins - {result['proteins']} gr/day\n"
                             f"Fats - {result['fat']} gr/day\n"
                             f"Carbohydrates - {result['carbohydrates']} gr/day")

        await message.answer('If you have another goal, then click on the desired button:')
        await Calculator.SendChoice.set()

    else:
        await message.answer('Please select an option from the options below:')


@dp.message_handler(state=Calculator.SendChoice)
async def get_answer_choice(message: types.Message, state: FSMContext):
    result = await state.get_data()
    if message.text in ("Slimming", "weight gain", "⬅Back"):
        if message.text == 'Slimming':
            await message.answer(f"Это твоя калорийность для похудения: {round(result['norm'] * 0.85)} cal")
            await message.answer(f"PFC:\n"
                                 f"Proteins - {round(result['proteins'] * 0.85)} gr/day\n"
                                 f"Fats - {round(result['fat'] * 0.85)} gr/day\n"
                                 f"Carbohydrates - {round(result['carbohydrates'] * 0.85)} gr/day")
        elif message.text == 'weight gain':
            await message.answer(f"Это твоя калорийность для weight gain: {round(result['norm'] * 1.15)} cal")
            await message.answer(f"PFC:\n"
                                 f"Proteins - {round(result['proteins'] * 1.15)} gr/day\n"
                                 f"Fats - {round(result['fat'] * 1.15)} gr/day\n"
                                 f"Carbohydrates - {round(result['carbohydrates'] * 1.15)} gr/day")
        else:
            await message.answer('Back to the main menu..', reply_markup=main_menu)
            await state.finish()

    else:
        await message.answer('Please select an option from the options below:')
