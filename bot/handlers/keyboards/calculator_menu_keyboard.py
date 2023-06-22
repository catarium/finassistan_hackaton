from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


cb = CallbackData('category', 'el_id')


async def calculator_menu_keyboard( ):
    buttons = [
        InlineKeyboardButton('Расчет точки безубыточности', callback_data='breakeven_point')
    ]
    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard

