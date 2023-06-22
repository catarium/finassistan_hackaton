from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData


async def graph_keyboard():
    buttons = [
        [InlineKeyboardButton('Расходы и доходы за год', callback_data='year_graph')],
        [InlineKeyboardButton('Расходы по категориям (год)', callback_data='cat_year_graph'),
         InlineKeyboardButton('Расходы по категориям (месяц)', callback_data='cat_month_graph')]
    ]

    keyboard = InlineKeyboardMarkup()
    for r in buttons:
        keyboard.row(*r)
    return keyboard
