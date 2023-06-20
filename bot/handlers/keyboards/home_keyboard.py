from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def home_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Мои финансы',
                                      callback_data='finances_menu'))
    keyboard.add(InlineKeyboardButton('Калькулятор',
                                      callback_data='calculator_menu'))
    return keyboard
