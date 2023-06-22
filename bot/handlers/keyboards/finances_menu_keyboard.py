from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData


f_cb = CallbackData('pagination', 'page')


async def finances_menu_keyboard(p):
    buttons = [
        [InlineKeyboardButton('<', callback_data=f_cb.new(page=p - 1)),
        InlineKeyboardButton('> ', callback_data=f_cb.new(page=p + 1)),],
        [InlineKeyboardButton('Добавить расходы', callback_data='add_expense'),
        InlineKeyboardButton('Добавить доходы', callback_data='add_income')],
        [InlineKeyboardButton('Экспорт данных', callback_data="finances_data")],
        [InlineKeyboardButton('На главную', callback_data='home')],
    ]
    row1 = [
        InlineKeyboardButton('<', callback_data=f_cb.new(page=p - 1)),
        InlineKeyboardButton('> ', callback_data=f_cb.new(page=p + 1)),
    ]
    row2 = [
        InlineKeyboardButton('Экспорт данных', callback_data="finances_data"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    for r in buttons:
        keyboard.row(*r)

    return keyboard
