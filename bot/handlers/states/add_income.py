from aiogram.dispatcher.filters.state import StatesGroup, State


class AddIncomeState(StatesGroup):
    sum = State()
