from aiogram.dispatcher.filters.state import StatesGroup, State


class AddIncomeState(StatesGroup):
    category = State()
    sum = State()
