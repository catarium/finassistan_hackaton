from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData


f_cb = CallbackData('pagination', 'page')

async def finances_menu_keyboard(p):
    buttons = [
        InlineKeyboardButton('<', callback_data=f_cb.new(page=p - 1)),
        InlineKeyboardButton('> ', callback_data=f_cb.new(page=p + 1)),
        InlineKeyboardButton('Вывод данных', callback_data="finances_data"),
        InlineKeyboardButton('Экспорт данных', callback_data="finances_data"),
        InlineKeyboardButton('Добавить расходы', callback_data='add_expense'),
        InlineKeyboardButton('Добавить доходы', callback_data='add_income'),
        InlineKeyboardButton('На главную', callback_data='home'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    return keyboard
