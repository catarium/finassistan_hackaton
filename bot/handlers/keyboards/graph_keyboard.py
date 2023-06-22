from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData


async def graph_keyboard():
    buttons = [
        [InlineKeyboardButton('Расходы и доходы за год (линейный)', callback_data='year_graph_line'),
         InlineKeyboardButton('Расходы и доходы за год (столбчатая)', callback_data='year_graph_bar')],
        [InlineKeyboardButton('Расходы по категориям за месяц', callback_data='cat_month_graph')],
    ]

    keyboard = InlineKeyboardMarkup()
    for r in buttons:
        keyboard.row(*r)
    return keyboard
