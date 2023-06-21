from aiogram.dispatcher.filters.state import StatesGroup, State


class AddExpenseState(StatesGroup):
    category = State()
    sum = State()
