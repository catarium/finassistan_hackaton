from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminState(StatesGroup):
    code = State()
    admin = State()
