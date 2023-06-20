from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def finances_menu_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Вывод данных',
                                      callback_data="finances_data"))
    keyboard.add(InlineKeyboardButton('Добавить расходы',
                                      callback_data='add_expense'))
    keyboard.add(InlineKeyboardButton('Добавить доходы',
                                      callback_data='add_income'))
    keyboard.add(InlineKeyboardButton('На главную',
                                      callback_data='home'))
    return keyboard