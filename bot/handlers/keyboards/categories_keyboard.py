from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


cb = CallbackData('category', 'el_id')


async def categories_keyboard(elements):
    buttons = [InlineKeyboardButton(el[1], callback_data=cb.new(el_id=el[0])) for el in elements]
    keyboard = InlineKeyboardMarkup()
    keyboard.add(*buttons)
    return keyboard
