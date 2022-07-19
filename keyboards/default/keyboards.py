from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data import main_menu_buttons, lecture_buttons, activity_types_buttons, complex_buttons, check_lists_buttons

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=main_menu_buttons[0])],
        [KeyboardButton(text=main_menu_buttons[1])],
        [KeyboardButton(text=main_menu_buttons[2])],
        [KeyboardButton(text=main_menu_buttons[3])],
        # [KeyboardButton(text=main_menu_buttons[4])],
        # [KeyboardButton(text=main_menu_buttons[5])],
        # [KeyboardButton(text=main_menu_buttons[6])],
        # [KeyboardButton(text=main_menu_buttons[7])],
    ]
)

activity_types_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=activity_types_buttons[0])],
        [KeyboardButton(text=activity_types_buttons[1])],
        [KeyboardButton(text=activity_types_buttons[2])],
        [KeyboardButton(text=activity_types_buttons[3])],
        [KeyboardButton(text=activity_types_buttons[4])],
        [KeyboardButton(text=activity_types_buttons[5])],
        [KeyboardButton(text=activity_types_buttons[6])],
        [KeyboardButton(text=activity_types_buttons[7])],
    ]
)

calculator_choice_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Slimming')],
        [KeyboardButton(text='weight gain')],
        [KeyboardButton(text='⬅Back')]
    ]
)

lectures = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=lecture_buttons[0])],
        [KeyboardButton(text=lecture_buttons[1])],
        [KeyboardButton(text=lecture_buttons[2])],
        [KeyboardButton(text=lecture_buttons[3])],
        [KeyboardButton(text=lecture_buttons[4])],
        [KeyboardButton(text=lecture_buttons[5])],
    ]
)

complex_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=complex_buttons[0])],
        [KeyboardButton(text=complex_buttons[1])],
        [KeyboardButton(text=complex_buttons[2])],
        [KeyboardButton(text=complex_buttons[3])],
        [KeyboardButton(text=complex_buttons[4])],
        [KeyboardButton(text=complex_buttons[5])],
        [KeyboardButton(text=complex_buttons[6])],
        [KeyboardButton(text=complex_buttons[7])],
    ]
)

check_lists_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=check_lists_buttons[0])],
        [KeyboardButton(text=check_lists_buttons[1])],
        [KeyboardButton(text=check_lists_buttons[2])],
    ]
)

